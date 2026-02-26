#!/usr/bin/env python3
"""
PreToolUse hook: Validates file paths follow lowercase-kebab-case conventions.
Blocks writes to incorrectly-named paths in transcripts/, analyses/, essays/.
"""
import sys
import json
import re


def check_path(file_path: str) -> tuple[bool, str]:
    """Check if a file path follows naming conventions. Returns (ok, message)."""
    # Only check paths within our managed directories
    managed_dirs = ("transcripts/", "analyses/", "essays/", "research/")
    rel_path = None
    for d in managed_dirs:
        idx = file_path.find(d)
        if idx != -1:
            rel_path = file_path[idx:]
            break

    if rel_path is None:
        return True, ""

    parts = rel_path.split("/")
    # Check each directory component (skip the file at the end)
    for part in parts[:-1]:
        if not part:
            continue
        # Directory names must be lowercase-kebab-case
        if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', part):
            suggestion = part.lower().replace(" ", "-").replace("_", "-")
            # Collapse multiple hyphens
            suggestion = re.sub(r'-+', '-', suggestion).strip("-")
            return False, (
                f"Directory '{part}' is not lowercase-kebab-case.\n"
                f"Expected: {suggestion}\n"
                f"Full path: {file_path}"
            )

    # Check file name patterns
    filename = parts[-1]
    if parts[0] == "transcripts":
        # transcript_<id>.md or NN_<slug>.md
        if not (re.match(r'^transcript_[a-zA-Z0-9_-]+\.md$', filename) or
                re.match(r'^\d{2}_[a-z0-9_]+\.md$', filename)):
            return False, (
                f"Transcript filename '{filename}' doesn't match expected patterns.\n"
                f"Expected: transcript_<video_id>.md or NN_<slug>.md\n"
                f"Full path: {file_path}"
            )
    elif parts[0] == "analyses":
        if not re.match(r'^analysis_[a-z0-9_-]+\.md$', filename):
            return False, (
                f"Analysis filename '{filename}' doesn't match expected pattern.\n"
                f"Expected: analysis_<keyword>_<video_id>.md\n"
                f"Full path: {file_path}"
            )
    elif parts[0] == "essays":
        if not re.match(r'^essay_[a-z0-9_-]+\.md$', filename):
            return False, (
                f"Essay filename '{filename}' doesn't match expected pattern.\n"
                f"Expected: essay_<keyword>_<date>.md\n"
                f"Full path: {file_path}"
            )

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
