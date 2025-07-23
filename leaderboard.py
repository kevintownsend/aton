"""Module for creating the leaderboard page."""

BEFORE = """<!DOCTYPE html>
<html>
  <head>
    <title>A to N Speed Typing Challenge</title>
  </head>
  <body>
"""
AFTER = """  </body>
</html>
"""

def leaderboard(conn):
    """Returns the leaderboard html page."""
    html = BEFORE
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    html += create_table(rows)
    html += AFTER
    # TODO: take cursor and output a leader board.
    return html

def create_table(rows):
    """Returns a formated table from the user data."""
    _ = rows
    return ""
