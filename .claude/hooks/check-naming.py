#!/usr/bin/env python3
"""
PreToolUse hook: Validates file paths follow naming conventions.
Blocks writes to incorrectly-named paths in research-topics/<topic>/<type>/.
"""
import sys
import json
import re


# Valid topics and content types
VALID_TOPICS = {"philosophy", "trading", "ai-agents"}
VALID_TYPES = {"transcripts", "analyses", "essays", "research"}

# Channel slugs that can appear in filenames
VALID_CHANNELS = {
    "michael-sugrue", "johnathan-bi",
    "axia-futures", "ict",
    "claude-code",
}


def check_path(file_path: str) -> tuple[bool, str]:
    """Check if a file path follows naming conventions. Returns (ok, message)."""
    # Only check paths within research-topics/
    idx = file_path.find("research-topics/")
    if idx == -1:
        return True, ""

    rel_path = file_path[idx:]
    parts = rel_path.split("/")
    # Expected: research-topics/<topic>/<type>/<filename>
    # Minimum: research-topics / topic / type / file = 4 parts

    if len(parts) < 4:
        return True, ""  # Not deep enough to validate yet

    topic = parts[1]
    content_type = parts[2]

    # Validate topic
    if topic not in VALID_TOPICS:
        return False, (
            f"Unknown topic '{topic}'.\n"
            f"Valid topics: {', '.join(sorted(VALID_TOPICS))}\n"
            f"Full path: {file_path}"
        )

    # Validate content type
    if content_type not in VALID_TYPES:
        return False, (
            f"Unknown content type '{content_type}'.\n"
            f"Valid types: {', '.join(sorted(VALID_TYPES))}\n"
            f"Full path: {file_path}"
        )

    # No subdirectories allowed under the content type
    if len(parts) > 4:
        return False, (
            f"No subdirectories allowed under research-topics/{topic}/{content_type}/.\n"
            f"Files go directly in the type folder (channel is encoded in filename).\n"
            f"Full path: {file_path}"
        )

    # Check filename patterns
    filename = parts[3]

    if content_type == "transcripts":
        # transcript_<channel>_<id>.md or NN_<channel>_<slug>.md
        if not (re.match(r'^transcript_[a-z0-9-]+_[a-zA-Z0-9_-]+\.md$', filename) or
                re.match(r'^\d{2}_[a-z0-9-]+_[a-z0-9_]+\.md$', filename)):
            return False, (
                f"Transcript filename '{filename}' doesn't match expected patterns.\n"
                f"Expected: transcript_<channel>_<video_id>.md or NN_<channel>_<slug>.md\n"
                f"Full path: {file_path}"
            )
    elif content_type == "analyses":
        if not re.match(r'^analysis_[a-z0-9-]+_[a-z0-9_-]+\.md$', filename):
            return False, (
                f"Analysis filename '{filename}' doesn't match expected pattern.\n"
                f"Expected: analysis_<channel>_<keyword>_<video_id>.md\n"
                f"Full path: {file_path}"
            )
    elif content_type == "essays":
        if not re.match(r'^essay_[a-z0-9-]+_[a-z0-9_-]+\.md$', filename):
            return False, (
                f"Essay filename '{filename}' doesn't match expected pattern.\n"
                f"Expected: essay_<channel>_<keyword>_<date>.md\n"
                f"Full path: {file_path}"
            )
    # research/ filenames are kept as-is (already descriptive)

    return True, ""


def main():
    input_data = json.load(sys.stdin)
    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})

    # Only check Write and Edit tools
    if tool_name not in ("Write", "Edit"):
        print(json.dumps({"decision": "approve"}))
        return

    file_path = tool_input.get("file_path", "")
    if not file_path:
        print(json.dumps({"decision": "approve"}))
        return

    ok, message = check_path(file_path)
    if ok:
        print(json.dumps({"decision": "approve"}))
    else:
        print(json.dumps({
            "decision": "block",
            "reason": f"Naming convention violation:\n{message}"
        }))


if __name__ == "__main__":
    main()
