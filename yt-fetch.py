#!/Users/rosa/video-essay-pipeline/.venv/bin/python3
"""YouTube Transcript Fetcher - v1+ API compatible, with Whisper fallback"""
import sys, re, argparse, os, tempfile, shutil
from datetime import datetime

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "youtube-transcript-api", "--break-system-packages", "-q"])
    from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url_or_id):
    for p in [r'(?:v=|\/v\/|youtu\.be\/|\/embed\/)([a-zA-Z0-9_-]{11})', r'^([a-zA-Z0-9_-]{11})$']:
        m = re.search(p, url_or_id)
        if m: return m.group(1)
    return url_or_id

def fetch_transcript(video_id, languages=None):
    if languages is None:
        languages = ['zh-Hans','zh-Hant','zh','en','ja','ko']
    ytt = YouTubeTranscriptApi()
    try:
        tlist = ytt.list(video_id)
        for lang in languages:
            try:
                t = tlist.find_transcript([lang])
                return {'language': t.language_code, 'is_generated': t.is_generated, 'entries': t.fetch()}
            except: continue
        for t in tlist:
            return {'language': t.language_code, 'is_generated': t.is_generated, 'entries': t.fetch()}
    except:
        try:
            f = ytt.fetch(video_id, languages=languages)
            return {'language': getattr(f,'language_code','unknown'), 'is_generated': getattr(f,'is_generated',False), 'entries': f}
        except Exception as e:
            print(f"No captions available: {e}")
            return None

def whisper_transcribe(video_id, model_name='medium'):
    """Download audio and transcribe with local Whisper."""
    tmp_dir = tempfile.mkdtemp(prefix='yt_whisper_')
    try:
        import yt_dlp
        audio_path = os.path.join(tmp_dir, 'audio.wav')
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(tmp_dir, 'audio.%(ext)s'),
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'wav'}],
            'quiet': True,
            'no_warnings': True,
        }
        print(f"Downloading audio for {video_id}...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'https://www.youtube.com/watch?v={video_id}'])

        if not os.path.exists(audio_path):
            for f in os.listdir(tmp_dir):
                if f.startswith('audio.'):
                    audio_path = os.path.join(tmp_dir, f)
                    break

        import whisper
        print(f"Transcribing with Whisper ({model_name})... this may take a while.")
        model = whisper.load_model(model_name)
        result = model.transcribe(audio_path)

        entries = []
        for seg in result['segments']:
            entries.append({'start': seg['start'], 'text': seg['text'].strip()})

        detected_lang = result.get('language', 'unknown')
        print(f"Whisper detected language: {detected_lang}")
        return {'language': detected_lang, 'is_generated': True, 'entries': entries, 'whisper': True}
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)

def fmt_ts(s):
    h,m,s = int(s//3600), int((s%3600)//60), int(s%60)
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"

def build_md(vid, res, ts=True):
    L = [f"# Transcript: {vid}\n",f"- **Video**: https://www.youtube.com/watch?v={vid}",
         f"- **Language**: {res['language']}",f"- **Auto-generated**: {'Yes' if res['is_generated'] else 'No'}"]
    if res.get('whisper'):
        L.append(f"- **Transcription**: Whisper (local)")
    L += [f"- **Fetched**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n","---\n"]
    for e in res['entries']:
        txt = (e.text if hasattr(e,'text') else e.get('text','')).replace('\n',' ').strip()
        if ts:
            st = e.start if hasattr(e,'start') else e.get('start',0)
            L.append(f"[{fmt_ts(st)}] {txt}")
        else: L.append(txt)
    return '\n'.join(L)

def main():
    p = argparse.ArgumentParser()
    p.add_argument('video')
    p.add_argument('--lang',nargs='+',default=None)
    p.add_argument('--output','-o',default=None)
    p.add_argument('--no-timestamps',action='store_true')
    p.add_argument('--whisper',action='store_true',help='Force Whisper transcription (skip YouTube API)')
    p.add_argument('--model',default='medium',help='Whisper model size (default: medium)')
    p.add_argument('--topic',default=None,help='Topic category (e.g. western-philosophy, psychology)')
    p.add_argument('--channel',default=None,help='Channel name slug (e.g. michael-sugrue)')
    a = p.parse_args()
    vid = extract_video_id(a.video)
    if a.output:
        out = a.output
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        if a.topic:
            t_dir = os.path.join(script_dir, "research-topics", a.topic, "transcripts")
        else:
            t_dir = os.path.join(script_dir, "transcripts")
        os.makedirs(t_dir, exist_ok=True)
        if a.channel:
            out = os.path.join(t_dir, f"transcript_{a.channel}_{vid}.md")
        else:
            out = os.path.join(t_dir, f"transcript_{vid}.md")
    print(f"Fetching transcript for: {vid}")
    if a.whisper:
        print("Whisper mode forced via --whisper flag.")
        res = whisper_transcribe(vid, a.model)
    else:
        res = fetch_transcript(vid, a.lang)
        if res is None:
            print("Falling back to Whisper transcription...")
            res = whisper_transcribe(vid, a.model)
    print(f"Found: {res['language']} ({'whisper' if res.get('whisper') else 'auto-generated' if res['is_generated'] else 'manual'})")
    md = build_md(vid, res, ts=not a.no_timestamps)
    with open(out,'w',encoding='utf-8') as f: f.write(md)
    print(f"Saved to: {out}")
    preview = ' '.join((e.text if hasattr(e,'text') else e.get('text','')) for e in list(res['entries'])[:20])
    print(f"\nPreview:\n{'-'*40}\n{preview[:500]}")

if __name__=='__main__': main()
