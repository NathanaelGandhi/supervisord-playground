import socket
import threading

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

def handle_client(conn):
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data: 
            break
        print ("received data:", data.decode('utf-8'), " on Thread ID:", threading.get_ident())
        conn.send(data)  # echo
    conn.close()

while True:
   conn, addr = s.accept()
   print ('Connection address:', addr)

   client_thread = threading.Thread(target=handle_client, args=(conn,))
   client_thread.start()

s.close()

