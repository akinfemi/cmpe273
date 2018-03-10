import zmq
import threading
import sys
import time

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
socket_sub = context.socket(zmq.SUB)
socket_push = context.socket(zmq.PUSH)

if (len(sys.argv[0:]) > 1):
    username = sys.argv[1]
    username = username.upper()
else:
    sys.exit()

# Define subscription and messages with prefix to accept.
socket_sub.setsockopt_string(zmq.SUBSCRIBE, username)
socket_sub.connect("tcp://127.0.0.1:4243") #data
socket_push.connect("tcp://127.0.0.1:4242") #commands

def init(user):
    print ("User [%s] Connected to server." % user)
    socket_push.send_string("User [%s] Connected to server." % user)

init(username)

while (True):
    message = input("[%s] > " % username)
    message = "%s %s" % (username, message)
    socket_push.send(message.encode('ascii'))