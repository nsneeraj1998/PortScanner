import socket
import threading
from queue import Queue

target= input("Enter Ip Address:")
queue4ports=Queue()
openPorts=[]
def portscan(port):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((target,port))
        return True
    except:
        return False

def queue2fill(ports):
    for port in ports:
        queue4ports.put(port)

def worker():
    while not queue4ports.empty():
        port=queue4ports.get()
        if portscan(port):
            print("Port {} is open.".format(port))
            openPorts.append(port)

ports=range(1,1024)
queue2fill(ports)

threads=[]

for t in range(1000):
    thread=threading.Thread(target=worker)
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("ports that are open:",openPorts)