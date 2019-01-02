#Authentication API
This is an authentication api which functions off of principles of the Diffie Hellman key exchange

With this authentication backend, you will not need to store any passwords, only server side secrets which are useless without the user secret and pin both of which are changed after every authentication.

##How it works
The authentication process is done by comparing a common secret hash (created by a user and server secret) to a user hash.
Created by Zach Leong