#!/usr/bin/env python3
"""
Granola → Slack Daily Summary Runner
Chief of Staff for Manan Kothari, PM at Homebase

This is the entry point called by the Cursor Automation cron (0 0 * * * UTC = 5pm PT).
It:
  1. Queries Granola for today's meetings (via the Granola MCP / Cursor tool integration)
  2. Parses decisions, rationale, and action items
  3. Calls daily_summary.py to send the Slack DM

Since Granola data must come through the Cursor automation environment (MCP tool calls
happen at the agent level, not subprocess level), this script accepts pre-parsed data
via the GRANOLA_DATA environment variable. The automation agent itself queries Granola,
formats the JSON, and injects it before calling this script.

See README.md for full setup instructions.
"""
# This file documents the integration contract. The actual execution flow is:
#   Cursor Automation Agent (has Granola MCP access)
#     → queries Granola for today's meetings
#     → formats as GRANOLA_DATA JSON
#     → runs: GRANOLA_DATA='[...]' python3 daily_summary.py
