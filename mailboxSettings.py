#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 08:16:17 2018

@author: rgarzon
"""

POP3_SERVER = ""
POP3_SSL_PORT = ""
POP3_LOGIN = ""
POP3_PWD = ""


class MailboxSettings:
    
    
    """
    Used to store the configuration of a POP3 connection to the mailbox
    """
    
#    def __init__(self, POP3server,login,pwd):
#        self.POP3server = POP3server
#        self.login = login
#        self.pwd = pwd
    
    def __init__(self):
        self.POP3server = POP3_SERVER
        self.login = POP3_LOGIN
        self.pwd = POP3_PWD
        self.port = POP3_SSL_PORT
        
    def getPop3Server(self):
        return self.POP3server
    
    def getPop3Login(self):
        return self.login
    
    def getPop3Pwd(self):
        return self.pwd
    
    def getPop3SSLPort(self):
        return self.port
    
