# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
from time import sleep
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    img = frame.array
    # show the frame
    # cv.imshow("Frame", img )

    # Detect yellow/orblue
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # lower_yellow = np.array([20, 100, 100])
    # upper_yellow = np.array([30, 255, 255])
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([120, 255, 255])

    # Createsa a mask wher pixels in range of color are 1(white) and out of range are 0 (black)
    # mask = cv.inRange(hsv, lower_yellow, upper_yellow)
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # Image refining
    kernel = np.ones((5, 5), np.uint8)
    opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    # cv.imshow('opening',opening)

    # bitwise and of the mask
    res = cv.bitwise_and(img, img, mask=opening)

    # cv.imshow('OG',img)
    # cv.imshow('mask',mask)
    cv.imshow('res', res)

    # resize image
    # scale_percent = 200  # percent of original size
    # width = int(img.shape[1] * scale_percent / 100)
    # height = int(img.shape[0] * scale_percent / 100)
    # dim = (width, height)
    # resized = cv.resize(res, dim, interpolation=cv.INTER_AREA)
    # cv.imshow('smaller.jpg',resized)

    # Threshold to make image binary
    ret, thresh1 = cv.threshold(mask, 1, 255, cv.THRESH_BINARY)
    # Finds nonzero pixels from theshold
    nonzero = cv.findNonZero(mask)
    # Takes the mean of the array for coordinates
    xy = cv.mean(nonzero)
    x = round(xy[0], 2)
    y = round(xy[1], 2)

    # print the dimensions of the shape
    height = img.shape[0]
    width = img.shape[1]
    fieldView = 52
    center = width / 2
    ratio = (center - x) / (width / 2)
    angleToObject = fieldView / 2 * ratio
    angleToObject = round(angleToObject, 2)
    # Convert to radians
    angleToObject = angleToObject

    # print("x"+str(x))
    # print("Ratio"+str(ratio))

    if x == 0 and y == 0:
        print("No Markers Found")
    else:
        print("Angle From Center" + str(angleToObject))

    key = cv.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

