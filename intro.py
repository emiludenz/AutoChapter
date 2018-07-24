#!/usr/bin/env python3
#import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import cv2
import os

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def get_video_frames(video='voy_intro.mp4'):
    #TODO: Yield a frame from video file
    cap = cv2.VideoCapture(video)
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
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


def compare(video1,video2):
    for frame in get_video_frames(video1):
        for f in get_video_frames(video2):
            if mse(frame,f) > 500:
                print("yeah!")
            else:
                print("Nope!")

def main():

    video_frames("Bobs.Burgers.S08E02/Bobs.Burgers.S08E02.mkv")
    video_frames("Bobs.Burgers.S08E03/Bobs.Burgers.S08E03.mkv")
    #make_dir()
    #get_video_frames()
    #compare()
    return 0


if __name__ == "__main__":
    main()