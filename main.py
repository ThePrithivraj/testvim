from ultralytics import YOLO

# Initialize the model
model = YOLO('C:\\Users\\thepr\\OneDrive\\Desktop\\Vimarsh\\YOLO Model\\Vandalism YOLO.pt')

# This function will be triggered when the "Process Video" button is clicked
def process_video(video_file):
    # Assuming the video file is passed as a path (make sure to adjust how the file is received)
    results = model(source=video_file, show=True, conf=0.75, save=True)
    # Further processing (saving output or displaying results)
    return results
