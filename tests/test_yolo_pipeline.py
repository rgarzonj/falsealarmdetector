#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 22:29:54 2018

@author: rgarzon
"""

import unittest
from imageFile import ImageFile
from yolo_pipeline import YoloClassifier

import os


class Testr(unittest.TestCase):
        
    def test_findPersonInPicture_with_PersonEasy(self):
        self.image_with_person = ImageFile('image_with_person2.jpg','./images/image_with_person2.jpg')
        self.assertTrue(YoloClassifier().findPersonInPicture(self.image_with_person))

    def test_findPersonInPicture_without_Person(self):
        self.image_without_person = ImageFile('./images/image_without_person.jpg')
        self.assertFalse(YoloClassifier().findPersonInPicture(self.image_without_person))

    def test_findPersonInPicture_with_PersonDifficult(self):
        self.image_with_person = ImageFile('image_with_person_difficult.jpg','./images/image_with_person_difficult.jpg')
        self.assertTrue(YoloClassifier().findPersonInPicture(self.image_with_person))

    def test_findPersonInPicture_with_PersonEasy2(self):
        self.image_with_person = ImageFile('./images/image_with_person9.jpg')
        self.assertTrue(YoloClassifier().findPersonInPicture(self.image_with_person))

    def test_getParentDir(self):
        cwd = os.getcwd()
        if (cwd.endswith('/tests')):
            parDir = os.path.abspath(os.path.join(cwd, ".."))
            weights_file = os.path.join(parDir,'yolo/YOLO_small.ckpt')
        else:
            weights_file = os.path.join(cwd,'yolo/YOLO_small.ckpt')
        self.assertTrue(os.path.isfile(os.path.isfile(weights_file)))
        
if __name__ == '__main__':
    unittest.main()