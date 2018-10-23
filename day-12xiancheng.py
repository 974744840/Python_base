import threading
import time
'''
方式一：类实现线程
1.继承父类的MyThread
2.重写run方法
3.start方法启动
'''
# class MyThread(threading.Thread):   #继承父类方法
#     def run(self):
#         for i in range(1,11):           #循环遍历
#             print(threading.current_thread().getName(),i)#显示线程+数字
#             time.sleep(0.1)     #延时，定时器函数
# t1=MyThread()       #MyThread类的对象t1
# t1.setName("线程1")   #线程名字
# t1.start()              #启动
# #新建线程2
# t2=MyThread()       #MyThread类的对象t1
# t2.setName("线程2")   #线程名字
# t2.start()              #启动
'''
方式二：类实现线程
target: 线程调用的对象,就是目标函数.
name: 为线程起个名字.
args: 为目标函数传递实参, 元组.
kwargs: 为目标函数关键字传参, 字典.
'''
def action():
    for  i in range(1,11):
        print(threading.current_thread().getName(),i)
        time.sleep(0.1) #睡眠
# 子线程
# 创建线程
t1=threading.Thread( target=action,name="线程1")
# 启动线程
t1.start()
# 创建线程
t2=threading.Thread( target=action,name="线程2")
# 启动线程
t2.start()
# 主线程
for i in range (1,11):
    print(threading.current_thread().getName (), i)
    time.sleep(0.1)  # 睡眠 单位秒：
print("线程数量:",threading.activeCount())

