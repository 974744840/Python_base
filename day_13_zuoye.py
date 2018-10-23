#利用生产消费者模式，取钱要先看银行类中有钱没。
#定义银行类
import threading
import time
p=2000         #创建个人银行存款默认为2000
lock=threading.Condition()  #创建生产消费者模式
class Consumer(threading.Thread):
    def run(self):
        global p,lock
        while True:
            lock.acquire()
            if p<100:
                p+=3000
                print(self.getName(),'余额不足100。我正在努力赚钱，现在卡里余额：',p)
                lock.notify()
            else:
                print(self.getName(),':余额充足。我要放个假，现在卡余额：',p)
                lock.wait()
            lock.release()
            time.sleep(1)
#定义存款类
class Bank(threading.Thread):
    def run(self):
        global p,lock
        while True:
            lock.acquire()
            if p>=100:
                p-=500
                print(self.getName(),'用户取走100元，现在卡里余额：',p)
                lock.notify()
            else:
                print(self.getName(),'卡里余额不足。取不出钱了，现在卡余额：',p)
                lock.wait()
            lock.release()
            time.sleep(1)
for i in range(1,2):
    I=Consumer()
    I.setName('给女朋友取钱：')
    I.start()
for i in range(1,2):
    B=Bank()
    B.setName('银行提款机：')
    B.start()