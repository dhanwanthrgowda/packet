import cv2

def list_cameras():
    # Get a list of all available cameras
    index = 0
    all_cams = []
    while True:
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
        if not cap.read()[0]:
            break
        else:
            all_cams.append(index)
        cap.release()
        index += 1
    return all_cams

if __name__ == '__main__':
    cameras = list_cameras()
    print("Available cameras:", cameras)
    cap = cv2.VideoCapture(cameras[1])
