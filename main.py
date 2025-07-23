"""Main Python module for aton app."""
import os
from dotenv import load_dotenv

import libsql

from flask import Flask
from flask import request

from constants import DB_URL

import leaderboard

app = Flask(__name__)

load_dotenv()

db_token = os.environ.get('DB_AUTH_TOKEN')

conn = libsql.connect("libsql", sync_url=DB_URL, auth_token=db_token)


# Connect to the torso libsql database.
conn.execute(
        "CREATE TABLE IF NOT EXISTS users "
        "(id INTEGER, user TEXT, score FLOAT);")
conn.commit()
conn.sync()

def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/')
def index():
    """Return the static index.html page."""
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.route('/leaderboard')
def leaderboard_page():
    """Create the leaderboard page."""
    return leaderboard.leaderboard(conn)

@app.route('/submit_score', methods = ['POST'])
def submit_score():
    """Submit the score to the leaderboard."""
    data = request.get_json()
    # TODO: process data.
    print(data)
    return ""

def main():
    """The main entry point of the app."""

    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), debug=True)

if __name__ == '__main__':
    main()
