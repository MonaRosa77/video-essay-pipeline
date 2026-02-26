#!/bin/bash
# Video → Essay Pipeline Setup
# Run this once to set up the project structure

set -e

PIPELINE_DIR="$HOME/video-essay-pipeline"

echo "=== Setting up Video → Essay Pipeline ==="

# Create directory structure
mkdir -p "$PIPELINE_DIR"/{transcripts,analyses,essays}

# Copy the fetch script
cp "$(dirname "$0")/yt-fetch.py" "$PIPELINE_DIR/yt-fetch.py" 2>/dev/null || {
    echo "Note: Copy yt-fetch.py to $PIPELINE_DIR/ manually"
}

# Copy CLAUDE.md for Claude Code context
cp "$(dirname "$0")/CLAUDE.md" "$PIPELINE_DIR/CLAUDE.md" 2>/dev/null || {
    echo "Note: Copy CLAUDE.md to $PIPELINE_DIR/ manually"
}

# Install Python dependency
echo "Installing youtube-transcript-api..."
pip install youtube-transcript-api --break-system-packages -q 2>/dev/null || \
pip install youtube-transcript-api -q

# Add shell alias for quick access
SHELL_RC="$HOME/.bashrc"
[[ "$SHELL" == *"zsh"* ]] && SHELL_RC="$HOME/.zshrc"

if ! grep -q "yt-fetch" "$SHELL_RC" 2>/dev/null; then
    echo "" >> "$SHELL_RC"
    echo "# Video → Essay Pipeline" >> "$SHELL_RC"
    echo "alias yt-fetch='python $PIPELINE_DIR/yt-fetch.py'" >> "$SHELL_RC"
    echo "alias yt-dir='cd $PIPELINE_DIR'" >> "$SHELL_RC"
    echo "Added aliases: yt-fetch, yt-dir"
fi

echo ""
echo "=== Setup Complete ==="
echo ""
echo "Directory: $PIPELINE_DIR"
echo "  transcripts/  - Raw video transcripts"
echo "  analyses/      - Structured analyses"  
echo "  essays/        - Essay drafts"
echo ""
echo "Usage:"
echo "  yt-fetch <youtube_url>              # Fetch transcript"
echo "  yt-fetch <url> --no-timestamps      # Without timestamps"
echo "  yt-fetch <url> --lang zh en         # Specify languages"
echo "  yt-fetch <url> -o custom_name.md    # Custom output name"
echo ""
echo "With Claude Code:"
echo "  cd $PIPELINE_DIR"
echo "  claude"
echo "  > Fetch and analyze: https://youtube.com/watch?v=..."
echo ""
echo "Reload your shell or run: source $SHELL_RC"
