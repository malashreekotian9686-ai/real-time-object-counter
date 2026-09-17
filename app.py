from flask import Flask, render_template, Response, jsonify, send_from_directory
import camera
import os
import datetime

from camera import generate_frames, save_screenshot
from camera import generate_frames, object_counts

import webbrowser
from threading import Timer

app = Flask(__name__)

# Track session start time
SESSION_START = datetime.datetime.now()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/counts')
def counts():
    return jsonify(camera.object_counts)

@app.route('/video_feed')
def video_feed():
    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

@app.route('/status')
def status():
    return jsonify({
        "running": camera.detection_running,
        "total": camera.total_objects,
        "screenshots": camera.screenshot_count
    })

@app.route('/start')
def start():
    camera.detection_running = True
    return "Detection Started"

@app.route('/stop')
def stop():
    camera.detection_running = False
    return "Detection Stopped"

@app.route('/capture')
def capture():
    print("Capture Route Called")
    if save_screenshot():
        print("Screenshot Saved Successfully")
        return "Screenshot Captured"
    print("Screenshot Failed")
    return "Failed to Capture"

@app.route('/captures')
def captures():
    files = []
    if os.path.exists("captures"):
        for f in os.listdir("captures"):
            if f.endswith(".jpg"):
                files.append(f)
    files.reverse()
    return jsonify(files[:6])

@app.route('/captures/all')
def captures_all():
    """Return ALL captured images for the gallery page."""
    files = []
    if os.path.exists("captures"):
        for f in os.listdir("captures"):
            if f.endswith(".jpg"):
                files.append(f)
    files.reverse()
    return jsonify(files)

@app.route('/captures/<filename>')
def get_capture(filename):
    return send_from_directory('captures', filename)

@app.route('/report')
def report():
    """Return session summary for the Reports page."""
    elapsed = datetime.datetime.now() - SESSION_START
    hours, rem = divmod(int(elapsed.total_seconds()), 3600)
    minutes, seconds = divmod(rem, 60)
    duration_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    # Count total captured images on disk
    cap_count = 0
    if os.path.exists("captures"):
        cap_count = len([f for f in os.listdir("captures") if f.endswith(".jpg")])

    return jsonify({
        "session_start": SESSION_START.strftime("%Y-%m-%d %H:%M:%S"),
        "duration": duration_str,
        "total_objects_detected": camera.total_objects,
        "screenshots_taken": cap_count,
        "detection_running": camera.detection_running,
        "object_breakdown": camera.object_counts
    })

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == '__main__':
    Timer(2, open_browser).start()
    app.run(debug=False)
