import cv2

# Open the default camera
cap = cv2.VideoCapture(0)

# Capture a single frame
ret, frame = cap.read()

# Save the frame as an image file
cv2.imwrite("captured_image.jpg", frame)

# Release the camera
cap.release()

print("Image saved as 'captured_image.jpg'")