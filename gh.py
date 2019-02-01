import socket

import threading

class thread():
    
    def listen(self):
        s = socket.socket()
        s.bind(("172.19.200.30",9095))
        s.listen(5)
        while 1==1:
            client,address=s.accept()
            print(str(address[0]))
            client.settimeout(60)
            client.send(b"You've connected")
            threading.Thread(target=self.recieve,args=(client,address)).start()
        
    def recieve(self,client,address):
        
        client.send(bytes(input(">"),"utf-8"))
        while True:
            
                
            data = client.recv(1024*2048)
            
            if data:
                f = open("scr.jpg","wb")
                f.write(data)
                f.close()
            print(str(address[0]))
            client.send(bytes(input(">"),"utf-8"))
            if data:
                # Set the response to echo back the recieved data 
                
                client.send(b"172.19.200.30"+b":"+b"_____________")
            else:
                raise error('Client disconnected')
            
thread().listen()
