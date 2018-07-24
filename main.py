#!/usr/bin/env python3
#import matplotlib.pyplot as plt
from video import video_frames
from os import listdir
import numpy as np
from PIL import Image


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    imageA = np.array(imageA)
    imageB = np.array(imageB)
    # TODO: Convert each image so they have the same dimensions
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare(video1,video2):
    for frame in listdir(video1):
        for f in listdir(video2):
            img1 = Image.open(video1 + "/" + frame)
            img2 = Image.open(video2 + "/" + f)
            if mse(img1,img2) > 500:
                print("yeah!")
            else:
                print("Nope!")


def main():

    #video_frames("Bobs.Burgers.S08E02/Bobs.Burgers.S08E02.mkv")
    #video_frames("Bobs.Burgers.S08E03/Bobs.Burgers.S08E03.mkv")

    #make_dir()
    #get_video_frames()
    compare("Frames-Bobs.Burgers.S08E02.mkv","Frames-Bobs.Burgers.S08E03.mkv")
    return 0


if __name__ == "__main__":
    main()