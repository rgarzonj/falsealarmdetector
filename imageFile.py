#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 08:19:39 2018

@author: rgarzon
"""

import matplotlib.image as mpimg
import os
import cv2

YOLO_W = 448
YOLO_H = 448
INTERVAL = 300

class ImageFile:

    def __init__(self, relativePath):
        
        self.absoluteFilename = os.path.abspath(relativePath)
        self.filename = os.path.basename(self.absoluteFilename)
        self.image = cv2.imread (self.absoluteFilename)
        
        #if self.filename.endswith('.jpg'):
        #    logging.info('Processing jpg image %s',self.absoluteFilename)
            
    def getImage(self):
        return self.image
    
    def getFilename(self):
        return self.filename

    def getMatplotlibImage(self):
        return mpimg.imread(self.absoluteFilename)

    def getImageSize(self):
        img = cv2.imread(self.absoluteFilename)
        height, width, channels = img.shape
        return (height,width,channels)
        
    
    def draw_result(self, img, result):
        for i in range(len(result)):
            x = int(result[i][1])
            y = int(result[i][2])
            w = int(result[i][3] / 2)
            h = int(result[i][4] / 2)
            cv2.rectangle(img, (x - w, y - h), (x + w, y + h), (0, 255, 0), 2)
            cv2.rectangle(img, (x - w, y - h - 20),
                          (x + w, y - h), (125, 125, 125), -1)
            lineType = cv2.LINE_AA if cv2.__version__ > '3' else cv2.CV_AA
            cv2.putText(
                img, result[i][0] + ' : %.2f' % result[i][5],
                (x - w + 5, y - h - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                (0, 0, 0), 1, lineType)

    def createYoloCandidates(self):
        #Check if 
        candidates = []
        h,w,c = self.getImageSize()
        print (h,w,c)
        y1 = 0
        y2 = YOLO_H
        i = 0
        while (y2 <h):
            x1 = 0
            x2 = YOLO_W                        
            while(x2<w):
                crop_img = self.image[y1:y2, x1:x2]
                candidates.append(crop_img)
                filename = 'candidate_'+str(i)+'.jpg'
                #cv2.imwrite(filename,crop_img)
                i = i + 1
                x1 = x1 + INTERVAL
                x2 = x2 + INTERVAL
            y1 = y1 + INTERVAL
            y2 = y2 + INTERVAL
        if (len(candidates)==0):
            candidates.append(self.image)
        return (candidates)
