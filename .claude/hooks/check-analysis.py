#!/usr/bin/env python3
"""
PostToolUse hook: Checks analysis files for required sections after writing.
Non-blocking — warns but does not prevent the save.
"""
import sys
import json
import re


REQUIRED_SECTIONS = [
    "Central Claim",
    "Supporting Arguments",
    "Evidence Quality",
    "Counter-Argument",
    "Notable Quotes",
]

# Sections that use "Original vs. Cited" or "Distinction:" pattern
ATTRIBUTION_PATTERNS = [
    r"Original vs\.",
    r"Distinction:",
    r"Cited Ideas",
]


def check_analysis(file_path: str, content: str) -> list[str]:
    """Check analysis content for required sections. Returns list of warnings."""
    warnings = []

    # Check required sections
    for section in REQUIRED_SECTIONS:
        if section.lower() not in content.lower():
            warnings.append(f"Missing section: '{section}'")

    # Check attribution section (any of the patterns)
    has_attribution = any(
        re.search(pattern, content, re.IGNORECASE)
        for pattern in ATTRIBUTION_PATTERNS
    )
    if not has_attribution:
        warnings.append("Missing section: 'Original vs. Cited Ideas' distinction")

    # Count counter-arguments
    counter_arg_section = re.split(
        r'##\s*Counter[- ]?Argument', content, flags=re.IGNORECASE
    )
    if len(counter_arg_section) > 1:
        # Count numbered items (1., 2., etc.) in the counter-arguments section
        # Take text up to the next ## heading
        ca_text = re.split(r'\n##\s', counter_arg_section[1])[0]
        numbered = re.findall(r'^\s*\d+\.', ca_text, re.MULTILINE)
        if len(numbered) < 3:
            warnings.append(
                f"Counter-arguments section has {len(numbered)} items (minimum 3 recommended)"
            )

    return warnings


def main():
    input_data = json.load(sys.stdin)
    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})

    # Only check Write tool targeting analyses/
    if tool_name != "Write":
        print(json.dumps({"decision": "approve"}))
        return

    file_path = tool_input.get("file_path", "")
    if "/analyses/" not in file_path:
        print(json.dumps({"decision": "approve"}))
        return

    content = tool_input.get("content", "")
    if not content:
        print(json.dumps({"decision": "approve"}))
        return

    warnings = check_analysis(file_path, content)

    if warnings:
        warning_text = "\n".join(f"  - {w}" for w in warnings)
        print(json.dumps({
            "decision": "approve",
            "reason": f"Analysis completeness warnings:\n{warning_text}"
        }))
    else:
        print(json.dumps({"decision": "approve"}))


if __name__ == "__main__":
    main()
