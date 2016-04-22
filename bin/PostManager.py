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

import IDP_Post

class PostManager(object):
    def __init__(self):
        pass

    def fetchPosts(self):
        pass

    def instantiatePosts(self):
        pass

    def picklePosts(self):
        pass

    def pushPK(self): #To Database
        pass

    def deletePosts(self):
        pass
