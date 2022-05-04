# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
from time import sleep
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from smbus2 import SMBus
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

increments = 0 

failed = False
#lcd_columns = 16 #initialize the LCD display
#lcd_rows = 2
#i2c = board.I2C()
#lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

#lcd.clear() #clear display for printing
#lcd.color = [100, 0, 50] #make lcd a good color

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
#low iso values have less noise but do ot work well in low light conditions low = 100 high = 400:800
camera.iso = 100;

camera.awb_mode = 'off'
cross = 0
rg,bg = (0.9,1.9)
camera.awb_gains = (rg,bg)
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
    
    top_xOG = 1
    top_yOG = 205
    bot_xOG = 640
    bot_yOG = 479
    
    cropped_imgOG = img[top_yOG:(top_yOG+bot_yOG),
                          top_xOG:(top_xOG+bot_xOG)]
    
    kernel = np.ones((5, 5), np.uint8)
    cropped_imgOG = cv.dilate(cropped_imgOG, kernel)
    cropped_imgOG = cv.dilate(cropped_imgOG, kernel)

    #img[0:130, 0:640] = {0,0,0}
    # Detect yellow/orblue
    hsv = cv.cvtColor(cropped_imgOG, cv.COLOR_BGR2HSV)
    # lower_yellow = np.array([20, 100, 100])
    # upper_yellow = np.array([30, 255, 255])
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([120, 255, 255])

    # Createsa a mask wher pixels in range of color are 1(white) and out of range are 0 (black)
    # mask = cv.inRange(hsv, lower_yellow, upper_yellow)
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # Image refining
    opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    
    # cv.imshow('opening',opening)

    # bitwise and of the mask
    res = cv.bitwise_and(cropped_imgOG, cropped_imgOG, mask=opening)

    #cv.imshow('OG',img)
    # cv.imshow('mask',mask)
    
    
    
    
    #If you do not want to see what the camera is detecting just comment this out
    cv.imshow('res', res)

    # This will resize the displayed image however it does slow down the program since this is done for every frame
    
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
    height = cropped_imgOG.shape[0]
    width = cropped_imgOG.shape[1]
    
    fieldViewX = 52
    centerX = width / 2
    ratioX = (x - centerX) / (width / 2)
    angleToObjectX = fieldViewX / 2 * ratioX
    #angleToObjectX = int(round(angleToObjectX, 2))
    # Now in range -26 : 26
    #angleToObjectX = angleToObjectX
    
    fieldViewY = 40
    centerY = height / 2
    ratioY = (centerY - y) / (height / 2)
    angleToObjectY = fieldViewY / 2 * ratioY
    angleToObjectY = int(round(angleToObjectY, 2))
    # Now in range -20 : 20
    #angleToObjectY = angleToObjectY
    
    #if (angleToObjectX >= -10) and (angleToObjectX <= 10):
    #    angleToObjectX = angleToObjectX
    #else:
    #    angleToObjectX = 0
    
    
    
    
    

    gray = cv.cvtColor(cropped_imgOG, cv.COLOR_BGR2GRAY)
    #edges = cv.Canny(gray, 30, 100)
    thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]


    cnts = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        peri = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.03 * peri, True)
    if(len(approx) > 8):
        print("cross = " + str(cross))
        cross = 1      
            
    print('number of sides:',len(approx))
    print("Angle From CenterX" + str(angleToObjectX))
    
    
    #print("Angle From CenterY" + str(angleToObjectY))
    
    #if ((angleToObjectX > 0) and (angleToObjectY > 0)):
    #    angleToObject = 0
        
    #elif ((angleToObjectX < 0) and (angleToObjectY > 0)):
    #    angleToObject = 90
        
    #elif ((angleToObjectX < 0) and (angleToObjectY < 0)):
    #    angleToObject = 180
        
    #elif ((angleToObjectX > 0) and (angleToObjectY < 0)):
    #   angleToObject = 270
        
    #else: 
    #   angleToObject = 500
    
    #CROPPPED
    

    #r = cv.selectROI("select the area", img)

    # Crop image
    #top_x = int(r[0])
    #top_y = int(r[1])
    #bot_x = int(r[2] + r[0])
    #bot_y = int(r[3] + r[1])
    
    top_x = 1
    top_y = 430
    bot_x = 640
    bot_y = 479

    #print("topx" + str(top_x))
    #print("topy" + str(top_y))
    #print("botx" + str(bot_x))
    #print("boty" + str(bot_y))
    
    

    #cv.rectangle(IMAGE,(TOPLEFT COORDS),(BOTRIGHT COORDS),(RGB),PIXELS)
    final = cropped_imgOG.copy()
    cv.rectangle(final,(top_x,top_y),(bot_x,bot_y),(0,255,0),1)

    #print(final.shape)

    cropped_image = img[top_y:(top_y+bot_y),
                          top_x:(top_x+bot_x)]

    #cv.imshow('COG',cropped_image)

    cropped_hsv = cv.cvtColor(cropped_image, cv.COLOR_BGR2HSV)
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([120, 255, 255])
    cropped_mask = cv.inRange(cropped_hsv, lower_blue, upper_blue)
    cropped_res = cv.bitwise_and(cropped_image,cropped_image, mask= cropped_mask)

    #cv.imshow('Cmask',cropped_mask)
    #cv.imshow('Cres',cropped_res)


    #print("cropped image dimesnions" + str(cropped_image.shape))

    # Threshold to make image binary
    ret, thresh2 = cv.threshold(cropped_mask, 1, 255, cv.THRESH_BINARY)
    # Finds nonzero pixels from theshold
    cropped_nonzero = cv.findNonZero(thresh2)
    # Takes the mean of the array for coordinates
    croppped_xy = cv.mean(cropped_nonzero)
    cropped_x = round(croppped_xy[0], 2)
    cropped_y = round(croppped_xy[1], 2)

    print("mean coords for cropped" + "(", cropped_x, ", ", cropped_y, ")")
    
    cv.imshow('final', final)

    if cropped_x == 0 and cropped_y == 0:
        print("no color")
    #ENDCROPPED

    # print("x"+str(x))
    # print("Ratio"+str(ratio))
    
    if x == 0 and y == 0:
        print("No Markers Found")
        if(failed == False): #if a number was printed before, clear the screen for printing
            #lcd.clear()
            failed = True
        
        #lcd.message = "No target Found"
    else:
        #ALEX !!!!!!!!!!!!!!! THIS IS THE ANGLE FROM THE CENTER OF THE CAMERA!
        print("Angle From Center" + str(angleToObjectX))
        bus = SMBus(1)
        increments = int(round(((angleToObjectX+27)/0.21568627),0))
        data = [increments, cross]
        #if cropped_x == 0 and cropped_y == 0:
        #    try:
        #        bus.write_byte_data(4, 1, increments) #write the given number to offset 0
                
        #    except IOError:
        #        print("Failed to connect to I2C bus. Trying again\n")
        #    bus.close()
        #    if(failed == True): #if a failure message was printed, clear screen for printing numbers
                #lcd.clear()
        #        failed = False
        
        try:
            bus.write_i2c_block_data(4, 1, data) #write the given number to offset 0
                
        except IOError:
            print("Failed to connect to I2C bus. Trying again\n")
        bus.close()
        if(failed == True): #if a failure message was printed, clear screen for printing numbers
                #lcd.clear()
                failed = False
        
        #lcd.message = str(round(angleToObjectX,2))
        
        
        print("----------------------------------------------------------")
        
    
    key = cv.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

