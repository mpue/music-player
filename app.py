from flask import Flask, render_template, jsonify, send_from_directory
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MUSIC_DIR = "./music"
playlist = [file for file in os.listdir(MUSIC_DIR) if file.endswith(".mp3")]
current_index = 0

@app.route("/")
def index():
    return render_template("index.html", title=playlist[current_index] if playlist else "No Music", playlist=playlist)

@app.route("/play")
def play():
    return jsonify(status="playing", track=playlist[current_index])

@app.route("/stop")
def stop():
    return jsonify(status="stopped")

@app.route("/next")
def next():
    global current_index
    current_index = (current_index + 1) % len(playlist)
    return jsonify(status="playing", track=playlist[current_index])

@app.route("/prev")
def prev():
    global current_index
    current_index = (current_index - 1) % len(playlist)
    return jsonify(status="playing", track=playlist[current_index])

@app.route("/music/<filename>")
def serve_music(filename):
    return send_from_directory(MUSIC_DIR, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
