"""Main Python module for aton app."""
import os

from flask import Flask


app = Flask(__name__)


def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/')
def index():
    """Return the static index.html page."""
    f = open("static/index.html")
    return f.read()

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), debug=True)
