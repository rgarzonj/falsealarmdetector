#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 08:45:37 2018

@author: rgarzon
"""

import unittest
from email_manager import EmailManager
from mailboxSettings import MailboxSettings
from emailEntity import EmailEntity
from smtpSettings import SmtpSettings
import datetime

class TestEmailManager(unittest.TestCase):

    def test_sendEmail(self):
        eMailContent = EmailEntity('This is a test','incoming@lifteye.es','incoming@lifteye.es','This is the body',[],datetime.datetime.now())
        self.assertTrue(EmailManager().sendEmail(eMailContent,SmtpSettings()))             

     def test_sendEmailWithException(self):
        eMailContent = EmailEntity('This is a test','incoming@lifteye.es','incominglifteye.es','This is the body',[],datetime.datetime.now())
        self.assertFalse(EmailManager().sendEmail(eMailContent,SmtpSettings()))
    
    def test_sendEmailWithAttachmentsJPG(self):

        file1 = 'images/cat.jpg'
        file2 = 'images/person.jpg'
        attachments = []
        attachments.append(file1)
        attachments.append(file2)
        eMailContent = EmailEntity('This is a test','incoming@lifteye.es','incoming@lifteye.es','This is the body',attachments,datetime.datetime.now())
        self.assertTrue(EmailManager().sendEmail(eMailContent,SmtpSettings()))             

    def test_getInfoFromEmail(self):
         res = EmailManager().getInfoFromEmail(0,MailboxSettings())         
         print (res.toJSONObject())
         self.assertTrue(len (res.getFrom())>0)

    def test_checkMailbox(self,):
        self.assertTrue(type (EmailManager().checkMailbox(MailboxSettings())),int)

    def test_getImagesFromEmail(self):
        res = EmailManager().getImagesFromEmail(0,MailboxSettings())        
        self.assertEqual(len(res),1)

    def test_getImagesFromEmail_withDelete(self):
        numEmails = EmailManager().checkMailbox(MailboxSettings())
        EmailManager().getImagesFromEmail(0,MailboxSettings(),True)
        self.assertEqual(EmailManager().checkMailbox(MailboxSettings()),numEmails-1)
#
    def test_prepareAlert(self):
         file1 = 'images/cat.jpg'
         file2 = 'images/person.jpg'
         attachments = []
         attachments.append(file1)
         attachments.append(file2)
         eMailContent = EmailEntity('This is a test','incoming@lifteye.es','incoming@lifteye.es','This is the body',attachments,datetime.datetime.now())
         res = EmailManager().prepareAlert(eMailContent)
         res_json = res.toJSONObject()
         self.assertEqual(res_json['To'],"incoming@lifteye.es")

if __name__ == '__main__':
    unittest.main()