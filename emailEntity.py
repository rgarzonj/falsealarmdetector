#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 09:23:49 2018

@author: rgarzon
"""

class EmailEntity:
    
    def __init__(self, subject,fromField,to,body,attachments,date):
        self.subject = subject
        self.fromField = fromField      
        self.to = to
        self.body = body
        self.attachments = attachments
        self.date = date
        
    def getSubject(self):
        return self.subject
    
    def getFrom(self):
        return self.fromField
    
    def getTo(self):
        return self.to
    
    def getBody(self):
        return self.body
        
    def getAttachments(self):
        return self.attachments
    
    def getDate(self):
        return self.date
    
    def toJSONObject(self):
        result = {'Subject' : self.subject,
                  'From': self.fromField,
                  'To': self.to,
                  'Body': self.body,
                  'Date': self.date
                  }
        return result