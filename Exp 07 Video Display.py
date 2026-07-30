import cv2

# Open the default webcam
cap = cv2.VideoCapture(0)

# Check if webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Controls:")
print("N - Normal Mode")
print("S - Slow Motion")
print("F - Fast Motion")
print("Q - Quit")

mode = "Normal"
frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame.")
        break

    # Display current mode on the video
    cv2.putText(frame, "Mode: " + mode, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2)

    # ---------------- NORMAL ----------------
    if mode == "Normal":
        cv2.imshow("Webcam Video", frame)
        key = cv2.waitKey(1) & 0xFF

    # ---------------- SLOW MOTION ----------------
    elif mode == "Slow":
        cv2.imshow("Webcam Video", frame)
        key = cv2.waitKey(100) & 0xFF      # 100 ms delay

    # ---------------- FAST MOTION ----------------
    elif mode == "Fast":
        frame_count += 1

        # Skip every alternate frame
        if frame_count % 2 == 0:
            continue

        cv2.imshow("Webcam Video", frame)
        key = cv2.waitKey(1) & 0xFF

    # --------- Change Modes ----------
    if key == ord('n') or key == ord('N'):
        mode = "Normal"

    elif key == ord('s') or key == ord('S'):
        mode = "Slow"

    elif key == ord('f') or key == ord('F'):
        mode = "Fast"

    elif key == ord('q') or key == ord('Q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
