#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:59:21 2018

@author: rgarzon
"""

from mailboxSettings import MailboxSettings
from email_manager import EmailManager
from yolo_pipeline import YoloClassifier
from imageFile import ImageFile
from smtpSettings import SmtpSettings
import logging
import os

LOG_FILE = 'logs/activity.log'

if not os.path.exists(os.path.dirname(LOG_FILE)):
    os.makedirs(os.path.dirname(LOG_FILE))

# Pre-configure the logging
FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=FORMAT,filename=LOG_FILE,level=logging.DEBUG)

#TODO Review error in log about NoneType

def main():
    logging.info('************* BEGIN check_false_alarms.py ************')
    mailManager = EmailManager()
    #Count number of emails

    numMails = mailManager.checkMailbox(MailboxSettings())
    logging.info('Found %s emails',str(numMails))
    if (numMails>0):
        yolo = YoloClassifier()
    #For every email
    if (numMails>5):
        numMails = 5
        logging.info('Only 5 emails will be checked in this execution.')
    for i in range(numMails):
        #Get the pictures
        logging.info('**** Checking email with ID %i ****',i)
        eMailInfo = mailManager.getInfoFromEmail(i,MailboxSettings())
        images = eMailInfo.getAttachments()
        if (len(images)==0):
            logging.info('No images found in the email with ID %i',i+1)
        else:
            #For every image, call Yolo try to detect a person
            for oneImage in images:
                logging.info('Checking image %s',oneImage)
                if (yolo.findPersonInPictureWithCandidates(ImageFile(oneImage))==True):
                    logging.info('Found person in picture %s',oneImage)
                    #Send email to notify there is a real alert
                    #Prepare the contents of the alert
                    eMailContentAlert = mailManager.prepareAlert(eMailInfo)
                    #Send the email
                    mailManager.sendEmail(eMailContentAlert,SmtpSettings())
                    break
                else:
                    logging.info ('No person found in picture %s',oneImage)                
    #Remove the emails once they have been processed
    mailManager.multipleDeleteEmail(range(numMails),MailboxSettings())
    logging.info('************* END check_false_alarms.py ************')
if __name__ == '__main__':
    main()