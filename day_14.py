#HTTP
# import  socket
# import threading
#
# cli=socket.socket()
# cli.connect(("192.168.102.17",1027))
# print("连接服务器成功")
#
# flag = True
#
# def read():
#     global flag
#     while flag:
#         msg = cli.recv (1024).decode ()
#         if msg == "88"  :
#             flag = False
#         print ("服务器：", msg)
#
# threading.Thread(target=read).start()
#
# while flag:
#     smsg=input()
#     cli.send(smsg.encode())
# cli.close()

##UDP
# import  socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# for data  in ["a","b","c"]:
#     s.sendto( data.encode(),("127.0.0.1",9999))
# s.close()
import random
import datetime
import time
#随机数
print(random.random())  #输出1以内的小数
print(random.uniform(1,3)) #输出1-3的小数
print(random.randint(1,10)) #输出1-10的整数
print(time.time())  #返回时间戳
time.sleep(2)
print(time.time())
# 测试程序运行时间
b=time.time()
for i in range(1,101):
    print(i)
print('时间:',time.time()-b)
# 获取当前年
ltime=time.localtime() #返回当前时间
print(ltime)
print(ltime.tm_year)
# 结构化时间转字符串时间
print(time.strftime('%Y-%m-%d ', time.localtime()))
# 结构化时间转字符串时间
print(time.strftime('%Y-%m-%d  %X',time.localtime()))
# 获得系统时间
print(type(time.strftime('%Y-%m-%d  %X', time.localtime())))

'''
....未完待续
'''

#########装饰器###########
# #返回运行时间
def decorator(func):
    def wrapper(a):
        print("装饰器代码开始...") # 返回时间戳
        func(a)
        print("装饰器代码结束...")
    return  wrapper
b=time.time()
#执行过程:
@decorator
def  fun(m):
    for i in range(1,m):
        print(i)
fun(1001)
print('时间:',time.time()-b)
