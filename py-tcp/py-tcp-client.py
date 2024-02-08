import socket
import threading
from datetime import datetime

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print (MESSAGE)

def start_connection(magic_number):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    msg_str = str(magic_number) + ": " + MESSAGE
    s.send(msg_str.encode())
    data = s.recv(BUFFER_SIZE)
    s.close()
    print("received data:", data.decode('utf-8'), " on Thread ID:", threading.get_ident())

threads = []
for i in range(10):
    t = threading.Thread(target=start_connection(i))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

