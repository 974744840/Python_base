import socket
import  threading
# 一对一不限时聊天
server=socket.socket()
server.bind(("192.168.30.110",8888))
print("服务器启动.....")
server.listen(1)
sc, addr = server.accept ()
print(addr[0],"客户端连接成功")
flag = True
def read():
    global flag
    while flag:
        msg = sc.recv (1024).decode ()
        if msg == "88"  :
            flag = False
        print ("客户端：", msg)
threading.Thread(target=read).start()
while flag:
    smsg=input()
    sc.send(smsg.encode())

import  socket
import threading
cli=socket.socket()
cli.connect(("192.168.30.110",8888))
print("连接服务器成功")
flag = True
def read():
    global flag
    while flag:
        msg = cli.recv (1024).decode ()
        if msg == "88"  :
            flag = False
        print ("服务器：", msg)
threading.Thread(target=read).start()
while flag:
    smsg=input()
    cli.send(smsg.encode())
cli.close()
