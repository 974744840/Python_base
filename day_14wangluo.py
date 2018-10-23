# import socket
# import  threading
# # 一对一不限时聊天
# server=socket.socket()
# server.bind(("192.168.102.17",1027))
# print("服务器启动.....")
# server.listen(1)
# sc, addr = server.accept ()
# print(addr[0],"客户端连接成功")
#
# flag = True
#
# def read():
#     global flag
#     while flag:
#         msg = sc.recv (1024).decode ()
#         if msg == "88"  :
#             flag = False
#         print ("客户端：", msg)
#
# threading.Thread(target=read).start()
#
# while flag:
#     smsg=input()
#     sc.send(smsg.encode())
import  socket

# 协议版本4    UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",9999))
print("服务器启动....")
while True:
    data, addr = s.recvfrom (1024)
    print (data.decode ())





