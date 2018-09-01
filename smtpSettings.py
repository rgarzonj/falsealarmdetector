#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 08:16:17 2018

@author: rgarzon
"""

SMTP_SERVER = "YOUR_SMTP_SERVER_ADDRESS"
SMTP_PORT = "YOUR_SMTP_SERVER_PORT"
SMTP_LOGIN = "YOUR_SMTP_SERVER_LOGIN"
SMTP_PWD = "YOUR_SMTP_SERVER_PASSWORD"
SMTP_START_TLS = True

class SmtpSettings:
    """
    Used to retrieve emails through POP3 protocol and send emails via SMTP protocol
    """
    
    def __init__(self):
        self.smtpServer = SMTP_SERVER
        self.smtpPort = SMTP_PORT
        self.login = SMTP_LOGIN
        self.pwd = SMTP_PWD
        self.startTLS = SMTP_START_TLS
        
    def getSMTPServer(self):
        return self.smtpServer
    
    def getSMTPPort(self):
        return self.smtpPort
    
    def getSMTPLogin(self):
        return self.login
    
    def getSMTPPwd(self):
        return self.pwd
    
    def getSMTPStartTLS(self):
        return self.startTLS