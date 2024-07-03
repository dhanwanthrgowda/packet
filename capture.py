import cv2
import os

def capture_photos(folder_path, num_photos):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Open the default camera with a different backend (e.g., DirectShow)
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Capture photos
    for i in range(num_photos):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print(f"Error: Failed to capture image {i+1}.")
            continue

        # Save the frame
        photo_path = os.path.join(folder_path, f"photo_{i+1}.jpg")
        if frame is not None:
            cv2.imwrite(photo_path, frame)
        else:
            print(f"Error: Captured frame {i+1} is None.")

        # Wait for 1 second (1000 milliseconds)
        cv2.waitKey(1000)

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()

def create_video(folder_path, output_video_path):
    # Get the list of photo filenames
    photo_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
    photo_files.sort()

    if not photo_files:
        print("No photos found in the folder.")
        return

    # Read the first image to get the frame size
    first_image_path = os.path.join(folder_path, photo_files[0])
    frame = cv2.imread(first_image_path)
    if frame is None:
        print("Error: Unable to read the first image.")
        return
    
    height, width, layers = frame.shape
    frame_size = (width, height)

    # OpenCV VideoWriter settings
    fps = 1  # 1 frame per second
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, frame_size)

    # Combine photos into video
    for photo_file in photo_files:
        photo_path = os.path.join(folder_path, photo_file)
        frame = cv2.imread(photo_path)
        if frame is not None:
            out.write(frame)
        else:
            print(f"Error: Unable to read image {photo_file}.")

    # Release VideoWriter
    out.release()

if __name__ == "__main__":
    folder_path = "photos"
    num_photos = 10
    output_video_path = "output_video1.mp4"

    # Capture photos
    capture_photos(folder_path, num_photos)

    # Create video from photos
    create_video(folder_path, output_video_path)

    print("Video created successfully!")