#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:03:45 2018

@author: rgarzon
"""

import poplib
import os
from email import parser
import logging

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from emailEntity import EmailEntity

import datetime

class EmailManager:
    """
    Used to retrieve emails through POP3 protocol and send emails via SMTP protocol
    """
    
    def __init__(self, ):

        self.imagesFolder = "./downloaded_images"     
        if not os.path.exists(self.imagesFolder):
            os.makedirs(self.imagesFolder)
        self.allowed_mimetypes = ["image/gif", "image/png", "image/jpeg", "image/bmp", "image/webp"]


    def prepareAlert(self,originalEmailData):
        """
        Creates an alert email to be sent when a person has been detected in the picture.
        Args:
            to: Destination of the alert email.
            Attachments: Image files to be included in the alert email.
        Returns:
            True if the email was correctly sent.
        """
        eMailContent = EmailEntity('A person has been detected'
                                   ,'incoming@lifteye.es',originalEmailData.getFrom(),'A person was found in one of the pictures. See files attached.\nOriginal data \n' + str(originalEmailData.toJSONObject()),originalEmailData.getAttachments() ,datetime.datetime.now())
        return eMailContent
    
    def sendEmail(self,eMail,smtpSettings):
        """
        Sends an email
        Args:
            eMail: Email object with the contents of the email.
            smtpSettings: SmtpSettings objects containing the configuration to be
                used for the SMTP sending.
        Returns:
            True if the email was correctly sent.
        """

        # Create the container (outer) email message.
        msg = MIMEMultipart()
        msg['Subject'] = eMail.getSubject()
        # me == the sender's email address
        # family = the list of all recipients' email addresses
        msg['From'] = eMail.getFrom()
        msg['To'] = eMail.getTo()
        body = MIMEText(eMail.getBody(), 'plain')
        msg.attach(body)       
        # Assume we know that the image files are all in PNG format
        for file in eMail.getAttachments():
            # Open the files in binary mode.  Let the MIMEImage class automatically
            # guess the specific image type.
            with open(file, 'rb') as fp:
                img = MIMEImage(fp.read())
                msg.attach(img)

        # Send the email via our own SMTP server.
        s = smtplib.SMTP(smtpSettings.getSMTPServer(),smtpSettings.getSMTPPort())
        if (smtpSettings.getSMTPStartTLS()==True):        
            s.starttls()    
        try:
            s.login(smtpSettings.getSMTPLogin(),smtpSettings.getSMTPPwd())
            s.send_message(msg)
            ret = True
            logging.info("Sent email to %s",eMail.getTo())
        except Exception as inst:
            logging.info("ERROR SENDING email %s",inst)
            ret = False
        s.quit()
        return ret
    
    def checkMailbox(self,mailboxSettings):        
        """
        Opens mailbox via POP3 protocol and returns the number of emails
        Args:
            None
        Returns:
            The number of emails in the mailbox.
        """
        M = self._connectPOP3SSLMailbox(mailboxSettings)
        numMessages = len(M.list()[1]) 
        M.quit()
        return numMessages

    def deleteEmail(self,which,mailboxSettings):
        M = self._connectPOP3SSLMailbox(mailboxSettings)
        logging.info('Deleting email with ID %d',which+1)
        M.dele(which+1)
        M.quit()
        
    def multipleDeleteEmail(self,emailsList,mailboxSettings):
        M = self._connectPOP3SSLMailbox(mailboxSettings)
        for which in emailsList:
            M.dele(which+1)
            logging.info('Deleting email with ID %d',which+1)
        M.quit()
        
#    def getImagesFromEmail(self,which,mailboxSettings,remove=False,):
#        """    
#        Checks email with ID 
#        Args:
#            which: Id of the email to check for images.
#            mailboxSettings: POP3 configuration to be used.
#            remove: Wether to delete the email from the mailbox or not.
#        Returns:
#            Lift of attachments (file_paths) of type image that were found in the email.
#        """
#        M = self._connectPOP3Mailbox(mailboxSettings)
#        attachments = []
#        parserObj = parser.FeedParser()
#        for msg in M.retr(which+1)[1]:
#            parserObj.feed(msg.decode('UTF-8') + '\n')
#        root = parserObj.close()
#        for part in root.walk():
#            if part.get_content_type() in self.allowed_mimetypes:
#                name = part.get_filename()
#                logging.info("Found image with name %s",name)
#                data = part.get_payload(decode=True)
#                full_path = os.path.join(self.imagesFolder,name)
#                f = open(full_path,'wb')
#                f.write(data)
#                f.close()
#                attachments.append(full_path)
#        if (remove==True):
#            logging.info('Deleting email with ID %d',which+1)
#            M.dele(which+1)                    
#        return attachments

    def _connectPOP3Mailbox (self,mailboxSettings):
        """    
        Opens POP3 connection according to the mailboxSettings
        Args:
            mailboxSettings: POP3 Server, login, pwd 
        Returns:
            poplib.POP3 object with the connection opened, quit() should be called using it
        """
        M = poplib.POP3(mailboxSettings.getPop3Server())
        M.user(mailboxSettings.getPop3Login())
        M.pass_(mailboxSettings.getPop3Pwd())
        return M
    
    def _connectPOP3SSLMailbox (self,mailboxSettings):
        """    
        Opens POP3 SSL connection according to the mailboxSettings
        Args:
            mailboxSettings: POP3 Server, login, pwd 
        Returns:
            poplib.POP3 object with the connection opened, quit() should be called using it
        """
        M = poplib.POP3_SSL(mailboxSettings.getPop3Server(),mailboxSettings.getPop3SSLPort())
        M.user(mailboxSettings.getPop3Login())
        M.pass_(mailboxSettings.getPop3Pwd())
        return M
    
    def getInfoFromEmail(self,which,mailboxSettings):
        #Returns the information from an email
        """    
        Retrieves the email information 
        Args:
            which: Id of the email to check for images.
            mailboxSettings: POP3 configuration to be used.
            remove: Wether to delete the email from the mailbox or not.        
        Returns:
            EmailEntity object with the information from the email.
        """
        M = self._connectPOP3SSLMailbox(mailboxSettings)
        attachments = []
        parserObj = parser.FeedParser()
#        for msg in M.retr(which+1)[1]:
        for msg in M.retr(1)[1]:
            parserObj.feed(msg.decode('UTF-8') + '\n')
        root = parserObj.close()
        body = ""
        for part in root.walk():            
            if part.get_content_type() in self.allowed_mimetypes:
                name = part.get_filename()
                if (isinstance(name,str)):
                    logging.info("Found image with name %s",name)
                    data = part.get_payload(decode=True)
                    full_path = os.path.join(self.imagesFolder,name)
                    f = open(full_path,'wb')
                    f.write(data)
                    f.close()
                    attachments.append(full_path)
            else:
                body_candidate = part.get_payload(decode=True)
                if (isinstance(body_candidate,bytes)):
                    body = body + str(body_candidate,'UTF-8')
        M.quit()          
        eMailInfo = EmailEntity(root.get('Subject'),root.get('From').strip('<>,'),root.get('To').strip('<>,')
        ,body,attachments,root.get('Date'))
        return eMailInfo
                