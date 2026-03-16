#!/usr/bin/env python3
"""
Orchestration entry point for the Chief of Staff daily summary.

This script is called by the Cursor Automation cron (0 0 * * *).
It fetches today's Granola meetings via the MCP, formats them into
a structured JSON payload, and passes them to daily_summary.py.

For the automation to work, set SLACK_TOKEN in:
  Cursor Dashboard → Cloud Agents → Secrets

Usage:
  python run_daily_summary.py

Or with pre-built data (for testing):
  GRANOLA_DATA='[...]' python daily_summary.py
"""

# NOTE: In the Cursor Automation environment, Granola data is fetched
# via the Granola MCP tool (not a Python library). The automation agent:
#   1. Calls Granola-list_meetings for today's date
#   2. Calls Granola-get_meetings for each meeting ID
#   3. Formats the summaries into GRANOLA_DATA JSON
#   4. Calls daily_summary.py with GRANOLA_DATA set
#
# This file serves as documentation of that contract and can also be
# used for local testing by constructing GRANOLA_DATA manually.

import os
import subprocess
import sys
import json


def run_summary(granola_data: list | None = None):
    """Run daily_summary.py, optionally injecting granola_data."""
    env = os.environ.copy()
    if granola_data is not None:
        env["GRANOLA_DATA"] = json.dumps(granola_data)

    script = os.path.join(os.path.dirname(__file__), "daily_summary.py")
    result = subprocess.run([sys.executable, script], env=env)
    return result.returncode


if __name__ == "__main__":
    # When run directly without GRANOLA_DATA, daily_summary.py handles
    # date-aware fallbacks (SF offsite, weekends, etc.)
    sys.exit(run_summary())
