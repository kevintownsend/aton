"""Main Python module for aton app."""
import os
from dotenv import load_dotenv

import libsql

from flask import Flask

from constants import DB_URL


app = Flask(__name__)

load_dotenv()

db_token = os.environ.get('DB_AUTH_TOKEN')

conn = libsql.connect("libsql", sync_url=DB_URL, auth_token=db_token)

def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/')
def index():
    """Return the static index.html page."""
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.route('/leaderboard')
def leaderboard():
    """Create the leaderboard page."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    # TODO: create a proper leaderboard.
    return rows[0][1]

def main():
    """The main entry point of the app."""

    # Connect to the torso libsql database.
    conn.execute(
            "CREATE TABLE IF NOT EXISTS users "
            "(id INTEGER, user TEXT, score FLOAT);")
    conn.commit()
    conn.sync()

    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), debug=True)

if __name__ == '__main__':
    main()
