### Some fun with sockets

run the `echo_server.py` first by `python echo_server.py`
then run the `echo_client.py`.

It's an implementation of a a simple handshake by TCP4

### As you would notice the socket is gonna end after receiving the first client.

For that what we're gonna do is make a multi connections one. run the server first and then the client.

and it would send multiple data onto the server and respond.

Usage : `python multiple-connection-server.py` to run the server on port 4564

to run the client use `python multiple-connections-client.py 127.0.0.1 4564 2` the 127.0.0.1 represents the <IP_SERVER> 
and 4564 represents <PORT> and 2 represents how many number of connections you would like to make in our case it's `2`

Find the topic interesting, head over to : [Real Python](https://realpython.com/python-sockets/) for further reference