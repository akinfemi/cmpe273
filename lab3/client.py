import zmq
import sys, threading

context = zmq.Context()

socket_sub = context.socket(zmq.SUB)
socket_push = context.socket(zmq.PUSH)
socket_push.connect("tcp://127.0.0.1:4242")
socket_sub.connect("tcp://127.0.0.1:4243")

class Server(username, threading.Thread):
    def __init__(self, username):
      threading.Thread.__init__(self)
      self.username = username
      print('User [%s] Connected to the chat server' %s self.username)
      
    
    def run(self):
        while(True):
            message = sub.recv()
            all = message.decode().split(' ')
            if(all[0] != self.username):
                 print("\n"+data[1]+":"+data[2])

while (True):
    message=input("["%s"] > " % name)
    data={'name':name,'message':message}
    push.send_json(data)

if __name__ == '__main__' :
    if len(sys.argv[0:]) < 2:
        print("Usage: python3 client.py <UserName>")
        sys.exit()
    else:
        username = sys.argv[1]
        server = Server(username)