#from PIL import Image
import numpy as np
import cv2
import os

#TODO: Try implementing multithreading to speed up the process



def get_video_frames(video='voy_intro.mp4'):
    #TODO: Yield a frame from video file
    cap = cv2.VideoCapture(video)
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret and count < 5000:
            frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            cv2.imwrite("Frames/framed%d.jpg" % count, frame)  # save frame as JPEG file
            count += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


def video_frames(video='voy_intro.mp4'):
    # gets all frames and puts them in a folder
    cap = cv2.VideoCapture(video)
    count = 0
    video = video.split("/")[-1]
    while cap.isOpened():
        make_dir(video)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(f"Frames-{video}/frame-{count}.jpg", frame)  # save frame as JPEG file
            count += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


def make_dir(string):
    if f"Frames-{string}" not in os.listdir():
        os.mkdir(f"Frames-{string}")



