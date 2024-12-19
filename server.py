from flask import Flask, request, jsonify
from ultralytics import YOLO
import os

app = Flask(__name__)

# Load the YOLO model
model = YOLO('C:\\Users\\thepr\\OneDrive\\Desktop\\Vimarsh\\YOLO Model\\Vandalism YOLO.pt')


@app.route('/process_video', methods=['POST'])
def process_video():
    if 'video' not in request.files:
        return jsonify({"message": "No video file uploaded"}), 400

    video_file = request.files['video']
    video_path = os.path.join("uploads", video_file.filename)
    video_file.save(video_path)

    # Process the video using YOLO
    results = model(source=video_path, show=True, conf=0.75, save=True)

    # Return a response (you can return the processed video URL or a message)
    return jsonify({"message": "Video processed successfully", "processed_video_url": "/path/to/processed_video.mp4"})


if __name__ == '__main__':
    app.run(debug=True)
