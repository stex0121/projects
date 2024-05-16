import cv2
import numpy as np

# Function to calculate center of a bounding box
def center_handle(x, y, w, h):
    cx = x + w / 2.0
    cy = y + h / 2.0
    return cx, cy

# Read the input video
cap = cv2.VideoCapture('video.mp4')

# Initialize Background Subtractor
algo = cv2.createBackgroundSubtractorMOG2()

# Parameters for vehicle detection and counting
min_area = 1000  # Adjust this threshold according to your needs
count_line_position = 650
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
count_line_position = frame_height - frame_height // 3  # Line position set to bottom one-third of the frame height
offset = 6
counter = 0
crossed_cars = set()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply background subtraction
    mask = algo.apply(frame)

    # Perform morphological operations
    mask = cv2.erode(mask, np.ones((5, 5), np.uint8), iterations=1)
    mask = cv2.dilate(mask, np.ones((5, 5), np.uint8), iterations=1)

    # Invert the mask to get the foreground
    fg = cv2.bitwise_and(frame, frame, mask=mask)

    # Convert the foreground to grayscale
    gray = cv2.cvtColor(fg, cv2.COLOR_BGR2GRAY)

    # Find contours
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw line
    cv2.line(frame, (-225, count_line_position), (1500, count_line_position), (255, 127, 0), 3)

    # Process contours
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        area = cv2.contourArea(c)

        # Validate contour
        if area >= min_area:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Calculate center of the bounding box
            center = center_handle(x, y, w, h)

            # Check if the center is above the counting line
            if center[1] < count_line_position and center[1] > count_line_position - offset:
                # Check if the car has crossed the line
                if isinstance(center, tuple) and len(center) == 2:
                    counter+=1
                    print("Vehicle Count:", counter)
                    cv2.putText(frame, "Vehicle " + str(counter), (int(center[0]), int(center[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv2.putText(frame, "Counter: " + str(counter), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)  # Add this line to display the counter
                else:
                    print("Invalid center coordinates:", center)
    cv2.putText(frame, "Vehicle Count: " + str(counter), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
    cv2.imshow('DETECTOR', mask)
    cv2.imshow('Video Original', frame)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
