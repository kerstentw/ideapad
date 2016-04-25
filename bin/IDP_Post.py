#!usr/bin/python2.7

import hashlib
import db_helper #Has functions for interacting with test database
import os
import sys
import time, datetime
from constants import *



class Post(object):
    
    '''
    This class creates an ovject that keeps track of the posting
    dates and times.  It is what is read off of to insure that a 
    user gets paid, posts regularly, and keeps a running record
    of a user's stuff.

    '''

    def __init__(self, password = None):
        
        '''
        This constructor will create a password hash that can be
        used to verify user.
        '''

        if password: 
            self.passhash = hashlib.sha256(str(password)).hexdigest()

        else:
            self.passhash = hashlib.sha256("key").hexdigest()        

        datetime.MINYEAR = 2016
        self.creation_time = tuple(x for x in time.localtime()[0:5])
        
        self.hashlist = ['END'] # Treat as a reverse queue: front is oldest.  Tail is youngest
        
        self.last_post = self.creation_time
        self.current_time = self.creation_time
        self.payMe = True
        self.name = self.passhash
    
    def __setattr__(self,target,location):
        print "Attributes on {} cannot be set once instantiated.".format(self.name)    

    def __convertToDateTime(self,time_tuple):
        '''
        convert a time tuple into a datetime structure
        '''

        time_str = "datetime.datetime{}".format(time_tuple)
        datetime_obj = eval(time_str)
        print datetime_obj
        return datetime_obj

    def coerceCurrentAnchorChange(self,(yyyy,mm,dd,hh,ss),just_current = 1):
        
        '''
        FOR DEVELOPMENT/DEPLOYMENT TESTING ONLY!!!!!!!!!!!!!!!!!!!

        coerceCurrentAnchorChange((yyyy,mm,dd,hh,ss)[,just_current = 1])        

        for testing, allows an anchor to be changed from the shell
        takes a tuple of (yyyy,mm,dd,hh,ss) and if just current is
        set to 0, will rebuild the anchor (the last date of successful post.
        
        need to comment out self.updatePost in checkElapsedTime 

        '''
        
        self.current_time = (yyyy,mm,dd,hh,ss)

        if just_current == 0:
            self.last_post = self.current_time
        else:
            pass

    def updatePost(self):
        self.current_time = tuple(x for x in time.localtime()[0:5])


    def checkElapsedTime(self):
        self.updatePost()
        dt_last_post = self.__convertToDateTime(self.post_anchor)        
        dt_current = self.__convertToDateTime(self.current_time)
        elapsed = dt_current - dt_last_post        

        return elapsed.days       

    def postSuccessfullyMade(self):
        self.last_post = tuple(x for x in time.localtime()[0:5])

    def checkForPayment(self):
        elapse_check = checkElapsedTime()
        if elapse_check  == 0:
            self.payMe = True
            return self.payMe       
 
        elif elapse_check > 0:
            self.payMe = False
            return self.payMe

        else: # Implies error.  Assume status does not change.
            return self.payMe


    def reHash(self,new_pass):
        self.hashdict.append(self.passhash)
        self.passhash = hashlib.sha256(new_pass)


    def stat(self):
        self.updatePost()
        my_stats = { 'name'          : self.name,
                     'password_hash' : self.passhash,
                     'creation_date' : self.creation_time,
                     'last_post'     : self.last_post,
                     'last_checked'  : self.current_time,
                     'payable?'      : self.payMe
                   }

        return my_stats

    def delete(self,master = PICKLE_MASTER): #from constants library
        os.remove(os.path.join(PICKLE_MASTER,self.name))
        return self.name," Removed"
  
