from unicodedata import name
from flask import Flask, request
from persistence import retrieve, store

from urlShortener import shortenUrl

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method=="POST":
        original_url = request.form["url"]
        short_url = shortenUrl(original_url)
        store(original_url=original_url, short_url=short_url)
        return short_url
    else:
        short_url = request.args.get("url")
        return retrieve(short_url=short_url)

if name == "__main__":
    app.run(host='127.0.0.1', port=5000)