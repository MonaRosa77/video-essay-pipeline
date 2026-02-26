#!/Users/rosa/video-essay-pipeline/.venv/bin/python3
"""
List videos from a YouTube channel and optionally fetch their transcripts.
Usage:
  python3 yt-channel.py <channel>                              # all videos, newest first
  python3 yt-channel.py <channel> --sort popular --limit 20    # top 20 most viewed
  python3 yt-channel.py <channel> --sort popular --limit 20 --fetch  # top 20 + transcripts
  python3 yt-channel.py <channel> --limit 5 --fetch            # latest 5 + transcripts
"""
import sys, os, argparse, subprocess

try:
    import yt_dlp
except ImportError:
    print("Installing yt-dlp...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp", "-q"])
    import yt_dlp

def resolve_channel_url(channel):
    channel = channel.strip().rstrip("/")
    if channel.startswith("UC") and len(channel) == 24:
        return f"https://www.youtube.com/channel/{channel}/videos"
    elif channel.startswith("http"):
        if "/videos" not in channel:
            channel = channel.rstrip("/") + "/videos"
        return channel
    elif channel.startswith("@"):
        return f"https://www.youtube.com/{channel}/videos"
    else:
        return f"https://www.youtube.com/@{channel}/videos"

def list_videos(channel_url, limit=None):
    opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": False,
        "ignoreerrors": True,
        "skip_download": True,
    }
    if limit:
        opts["playlist_items"] = f"1:{limit}"

    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(channel_url, download=False)
        if info is None:
            return [], "Unknown Channel"
        videos = []
        for entry in info.get("entries", []):
            if entry is None:
                continue
            videos.append({
                "id": entry.get("id"),
                "title": entry.get("title", "Unknown"),
                "views": entry.get("view_count", 0) or 0,
                "published": entry.get("upload_date", ""),
                "duration": entry.get("duration", 0) or 0,
                "url": f"https://www.youtube.com/watch?v={entry.get('id')}"
            })
        return videos, info.get("channel", "Unknown Channel")

def fmt_views(n):
    if n >= 1_000_000: return f"{n/1_000_000:.1f}M"
    if n >= 1_000: return f"{n/1_000:.1f}K"
    return str(n)

def fmt_duration(s):
    if not s: return "?"
    h, m, sec = int(s//3600), int((s%3600)//60), int(s%60)
    if h: return f"{h}:{m:02d}:{sec:02d}"
    return f"{m}:{sec:02d}"

def main():
    p = argparse.ArgumentParser(description="List & fetch transcripts from a YouTube channel")
    p.add_argument("channel", help="Channel @handle, channel ID (UC...), or URL")
    p.add_argument("--sort", choices=["popular", "newest", "oldest"], default="newest",
                   help="Sort order (default: newest)")
    p.add_argument("--limit", type=int, default=None, help="Max videos (default: all)")
    p.add_argument("--fetch", action="store_true", help="Also fetch transcripts")
    p.add_argument("--lang", nargs="+", default=None, help="Preferred transcript languages")
    a = p.parse_args()

    channel_url = resolve_channel_url(a.channel)

    # For popular sort without limit, fetch everything then sort
    # For popular sort with limit, fetch extra to sort properly
    if a.sort == "popular" and a.limit:
        fetch_count = max(a.limit * 3, 100)
    else:
        fetch_count = a.limit  # None = all

    limit_label = str(a.limit) if a.limit else "all"
    print(f"Fetching {limit_label} videos from: {channel_url}")
    print(f"(this may take a moment...)\n")

    videos, channel_name = list_videos(channel_url, fetch_count)

    if not videos:
        print("No videos found. Check the channel name/ID.")
        sys.exit(1)

    # Sort
    if a.sort == "popular":
        videos.sort(key=lambda v: v["views"], reverse=True)
    elif a.sort == "oldest":
        videos.sort(key=lambda v: v["published"])

    # Trim to limit if set
    if a.limit:
        videos = videos[:a.limit]

    print(f"Channel: {channel_name}")
    print(f"Showing: {len(videos)} videos (sorted by {a.sort})\n")
    print(f"{'#':>3}  {'Views':>8}  {'Length':>8}  Title")
    print(f"{'─'*3}  {'─'*8}  {'─'*8}  {'─'*50}")

    for i, v in enumerate(videos, 1):
        views = fmt_views(v["views"])
        dur = fmt_duration(v["duration"])
        title = v["title"][:55]
        print(f"{i:>3}  {views:>8}  {dur:>8}  {title}")

    print()

    if a.fetch:
        print("=" * 60)
        print("Fetching transcripts...\n")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        fetch_script = os.path.join(script_dir, "yt-fetch.py")
        t_dir = os.path.join(script_dir, "transcripts")
        os.makedirs(t_dir, exist_ok=True)
        success, fail = 0, 0
        for v in videos:
            cmd = [sys.executable, fetch_script, v["url"],
                   "-o", os.path.join(t_dir, f"transcript_{v['id']}.md")]
            if a.lang:
                cmd += ["--lang"] + a.lang
            print(f"  [{success+fail+1}/{len(videos)}] {v['title'][:50]}...", end=" ")
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print("✓")
                success += 1
            else:
                print("✗ (no transcript)")
                fail += 1
        print(f"\nDone: {success} transcripts fetched, {fail} failed")
    else:
        print(f"To fetch transcripts, add --fetch")
        if a.limit:
            print(f"  python3 yt-channel.py {a.channel} --sort {a.sort} --limit {a.limit} --fetch")
        else:
            print(f"  python3 yt-channel.py {a.channel} --sort {a.sort} --fetch")

if __name__ == "__main__":
    main()
