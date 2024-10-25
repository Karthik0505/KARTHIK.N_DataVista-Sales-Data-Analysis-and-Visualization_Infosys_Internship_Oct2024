import cv2

video_path1 = "C://Users//KARTHIK//Downloads//854097-hd_1920_1080_25fps.mp4"
video_path2 = "C://Users//KARTHIK//Downloads//855564-hd_1920_1080_24fps.mp4"
video_path3 = "C://Users//KARTHIK//Downloads//853844-hd_1920_1080_25fps.mp4"

# Open video captures for each video file
cap1 = cv2.VideoCapture(video_path1)
cap2 = cv2.VideoCapture(video_path2)
cap3 = cv2.VideoCapture(video_path3)

# Check
if not (cap1.isOpened() and cap2.isOpened() and cap3.isOpened()):
    print("Error: Could not open one or more video files.")
    exit()

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('output1.avi', fourcc, 20.0, (640, 480))
out2 = cv2.VideoWriter('output2.avi', fourcc, 20.0, (640, 480))
out3 = cv2.VideoWriter('output3.avi', fourcc, 20.0, (640, 480))

display_size = (320, 240)

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    ret3, frame3 = cap3.read()

    if not ret1 or not ret2 or not ret3:
        print("Error: Failed to capture frame from one or more sources or end of video reached.")
        break

    frame1_resized = cv2.resize(frame1, display_size)
    frame2_resized = cv2.resize(frame2, display_size)
    frame3_resized = cv2.resize(frame3, display_size)

    out1.write(frame1)
    out2.write(frame2)
    out3.write(frame3)

    cv2.imshow('Video 1', frame1_resized)
    cv2.imshow('Video 2', frame2_resized)
    cv2.imshow('Video 3', frame3_resized)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cap3.release()
out1.release()
out2.release()
out3.release()
cv2.destroyAllWindows()