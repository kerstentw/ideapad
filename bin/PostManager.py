#!/usr/bin/Python2.7

#PostManager is a module for handling Posts.  It directly interfaces
# with the Post module and instances Posts
# It does:
#    -instantiate posts
#    -Pickle Posts
#    -Place pk files in db
#    -Manage Posts

# use post_instance.stat() to get a dump of a posts's 
#contents for db write.
# Purposely made the stat method a Python DataStruc in order to make it
# compatible with any db.

# Author: Tai Kersten
# Email: kerstentw@gmail.com

import os, sys
import hashlib
import pickle
from IDP_Post import *
    # instantiates the term 'Post' with all its methods.


#If a new instance, will create the home dir 
#necessary for the functioning of the manager

PICKLE_MASTER = "pk_jar"

if MASTER  not in os.listdir('.'):
    os.mkdir(PICKLE_MASTER)

else:
    pass

class PostManager(self):
    def __init__(self):
        pass

    def fetchPosts(self):
        pass

    def instantiatePosts(self):
        pass


class PickleManager(object):

    def __init__(self, master = PICKLE_MASTER:
        self.master = master

    def picklePosts(self,post_instance):
        '''
        This function pickles an instance of a post and writes it to the master
        folder defined above.
        '''

        temp_file = open(os.path.join(self.master,"{post_name}.pk".format(post_name = post_instance.name)),"w")
        unpickled_post = pickle.dump(post_instance,temp_file)
        temp_file.close()
        return "post saved"


    def viewPickles(self):
        return os.listdir(os.path.join(".","pk_jar"))    
        
    def retrievePickle(self, pickle_human_name):
        pass 

    def pushPK(self): #To Database
        pass

    def deletePickle(self):
        pass
