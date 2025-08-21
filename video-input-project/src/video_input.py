def get_video_file_path():
    """
    Prompt the user for a video file path and validate the input.
    Returns the valid video file path.
    """
    while True:
        video_path = input("Please enter the path to the video file: ")
        if os.path.isfile(video_path) and video_path.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            return video_path
        else:
            print("Invalid file path or file type. Please enter a valid video file.")

if __name__ == "__main__":
    video_file = get_video_file_path()
    print(f"Video file selected: {video_file}")