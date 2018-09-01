#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 08:19:39 2018

@author: rgarzon
"""

import matplotlib.image as mpimg
import os
import logging
        
class ImageFile:
    
    def __init__(self, absoluteFilename):
        
        self.filename = os.path.basename(absoluteFilename)
        self.absoluteFilename = absoluteFilename

        if self.filename.endswith('.jpg'):
            logging.info('Processing jpg image %s',absoluteFilename)
            

    def getFilename(self):
        return self.filename

    def getMatplotlibImage(self):
        return mpimg.imread(self.absoluteFilename)
