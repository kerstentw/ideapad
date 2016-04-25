# ideapad
An idea pad with built-in decentralized self-incentives



The bin folder holds all of the backend libraries.  Use these in conjunction
with whatever front end web app to create behaviors.

There are 2 implementations build in for code persistance without using 
user sessions (this is to ensure that all post dates and information
are fully controlled by the server.

Don't expose the bin folder to the web if possible.  

Implementation 1: 
	app uses the pickle to store user posts and 
check dates.  PostManager.py handles instantiating posts, calling
post methods, and de-pickling posts.  This is the pure python
implementation, I recommend using it with web.py or boilerplate
Django.

Default directory for storing pk files: pk_jar

This is stashed in the bin directory for safe keeping.

Implementation 2:
	The database handles the data and checks are maintained 
by making queries to the database.  





