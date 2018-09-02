#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 11:49:03 2018

@author: rgarzon
"""


import unittest
from imageFile import ImageFile


class Testr(unittest.TestCase):
    
    def test_createYoloCandidates(self):
        self.image_with_person = ImageFile('./images/image_with_person.jpg')
        res = self.image_with_person.createYoloCandidates()
        self.assertTrue(len(res)>0)
        
if __name__ == '__main__':
    unittest.main()