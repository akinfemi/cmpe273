import zmq
import time

context = zmq.Context()

socket_pub = context.socket(zmq.PUB)
socket_pull = context.socket(zmq.PULL)
socket_pull.bind("tcp://127.0.0.1:4242")
socket_pub.bind("tcp://127.0.0.1:4243")

while True:
    msg = pull.recv()
    pub.send(msg)
    time.sleep(1)