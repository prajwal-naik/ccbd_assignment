#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:16:38 2020

@author: prajwal
"""


import cv2
import numpy as np
import os
#from PIL import Image
# Read

images=[]
for filename in os.listdir("satellite/"):
        name=os.path.join("satellite",filename)
        images.append(name)
        
for filename in images:
    img = cv2.imread(filename)

    # convert to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    
    # mask of green (36,25,25) ~ (86, 255,255)
    # mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
    mask = cv2.inRange(hsv, (30, 25, 25), (100, 255,120))
    #mask = cv2.inRange(hsv, (10, 25, 25), (100, 255,100))
    
    ## slice the green
    imask = mask>0
    green = np.zeros_like(img, np.uint8)
    green[imask] = img[imask]
    
    black=0
    total=0
    for i in range(green.shape[0]):
        for j in range(green.shape[1]):
            total+=1
            if((green[i][j][0]==0) and (green[i][j][1]==0) and (green[i][j][2]==0)):    #counting pixels which are black 
                black+=1
            
    #print(black, total, total-black)
    percentage=int(((total-black)/total)*100)
    
    
    area=filename.split("\\")[1][:-4]
    line=filename+","+area+","+str(percentage)
    with open("report.csv", "a") as fp:
        print(line, file=fp)
        
        
    print(percentage)
    # save image
    
    cv2.imwrite("greens/"+area+'.jpg', green)
    
    
    
    
    
    
    
    
    
    
    '''count=0
    for i in range(hsv.shape[0]):
        for j in range(hsv.shape[1]):
            if(((hsv[i][j][0] <= 100) and (hsv[i][j][1] <= 255) and (hsv[i][j][2] <= 255)) and 
            ((hsv[i][j][0] >= 30) and (hsv[i][j][1] >= 25) and (hsv[i][j][2] >= 25))):
                count+=1
    print(count)'''
    
    
    '''im=Image.open("mathikere_g.jpg")
    for pixel in im.getData():
        total+=1
        if pixel is (0,0,0):
            black+=1
    print(total, black)
    '''