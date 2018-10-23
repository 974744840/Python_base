#方式一
# class UserDao:
#     __instance = None  #创建类属性
#     # 构造方法不能私有
#     def  __init__(self):
#         print("构造方法")
#     #创建静态方法，目的：为了类可以直接调用
#     @staticmethod
#     def  getInStance( ):
#         if UserDao.__instance is None:
#             UserDao.__instance = UserDao ()
#         return  UserDao.__instance
# #缺点：还可以new对象
# # dao1=UserDao()
# # dao2=UserDao()
# # dao3=UserDao()
#
#
# dao1=UserDao.getInStance()
# dao2=UserDao.getInStance()
# dao3=UserDao.getInStance()
# print(id(dao1))
# print(id(dao2))
# print(id(dao3))

#方式二
import  threading
import time
lock = threading.Lock()
class UserDao2:
    __instance = None
    def  __init__(self):
        print("构造方法")
    def __new__(cls):
        lock.acquire()
        if cls.__instance is None:
            cls.__instance=object.__new__(cls)
            time.sleep(0.1)
        lock.release()
        return cls.__instance
#测试
def test_singleton():
    print (id(UserDao2()))
for  i  in range(1,11):
    threading.Thread(target=test_singleton).start()

#死锁优化
import threading
import time
class Makeup(threading.Thread):
    name =None
    flag=None
    lock1=threading.Lock()#老大
    lock2=threading.Lock()#老二
    def doMakeup(self):
        if self.flag==1:
            self.lock1.acquire()
            print(self.name+'用口红')
            self.lock1.release()   #将这行代码放再64行处，就会出现死锁状态，两个线程只能掉用一个

            time.sleep(1)
            self.lock2.acquire()
            print(self.name+'用油')
            self.lock2.release()
        else:
            self.lock1.acquire()
            print(self.name+'用油')
            self.lock1.release()

            time.sleep(1)
            self.lock2.acquire()
            print(self.name+'用口红')
            self.lock2.release()
    def run(self):
        self.doMakeup()
m1=Makeup()
m1.flag=1
m1.name='大女儿'
#
m2=Makeup()
m2.flag=2
m2.name='二女儿'

m1.start()
m2.start()

###生产和消费者模式
import threading
import time
p=0   #包子数量
condition=threading.Condition() #也就是创建互斥对象进行 锁 等待 唤醒 的调用
#生产者类
class Producer(threading.Thread):
    def run(self):      #运行函数
        global p,condition #两个全局变量，一个是包子的数量，一个是线程的对象
        while True:
            condition.acquire()         #线程加锁
            if p<10:                #这里控制库存数量 如果小于10则:用notify激活该线程进行 P+=1
                p+=1
                print(self.getName(),"：库存不足(10-)。我努力生产了1件产品，现在产品总数量 ", p)
                condition.notify()
            else:                   #如果够了10个，跳到这里执行wait，进行等待
                print(self.getName(), "：库存充足(10+)。让我休息会儿，现在产品总数量 ", p)
                condition.wait()
            condition.release()     #进行解锁
            time.sleep(1)           #增加休眠时间
# #######消费者与上同理
class Consumer(threading.Thread):
    def run(self):
        global p,condition
        while True:
            condition.acquire()
            if p > 1:  # 如果有1个包子，我就买
                p -= 1
                print(self.getName(), "：我消费了1件产品，现在产品数量 ", p)
                condition.notify()  # 唤醒
            else:               #如果没有包子我就等
                print(self.getName(), "：只剩下1件产品，我停止消费。现在产品数量 ", p)
                condition.wait() # 等待
            condition.release()     #对整个程序加锁解锁控制
            time.sleep(1)
for i in range(1,20):
    t=Producer()
    t.setName('生产者'+str(i))
    t.start()
for i in range(1,2):
    c=Consumer()
    c.setName('消费者'+str(i))
    c.start()

###定时器
import threading
import time
def text():
    global t
    print('办理业务')
    t=threading.Timer(1,text) #定时每一秒执行一次该方法
    t.start()
text()
time.sleep(15)#总共执行15秒
t.cancel() #结束执行定时器

###消息队列
import queue
class job(object):
    def __init__(self,prioity,name):
        self.prioity=prioity
        self.name=name
        print('开始取号：',self.name)
    def __lt__(self, other):    #比较优先级
        return self.prioity>other.prioity
job1=job(100,'鑫鑫')  #实例化三个对象
job2=job(200,'淼淼')
job3=job(5,'森森')
q=queue.PriorityQueue()     #实例化优先级排序对象
q.put(job1)         #将要进行排序的对象添加到优先级对象里
q.put(job2)
q.put(job3)
while not q.empty(): #循环排列出优先级
    print('开始办理：',q.get().name)

class A:
    # 静态的类属性
    name="admin"
    def __init__(self, age):#构造方法和实例属性
        self.age = age
    # 静态方法
    @staticmethod
    def run():
        name='jjjjjjj'
        print("run.....",name,)

    @staticmethod
    def runn():
        name = 'jjjjjjj'
        
        print("run.....", name)
    # 实例方法
    def sing(self):
        print('sing...',self.name,self.run(),self.age) #实例方法调用静态属性和方法


a=A(50)         #实例化对象动态属性
a.run()         #实例对象调用静态方法
a.sing()        #实例对象调用动态方法
a.name='郭荣鑫'  #实例对象调用静态属性
a.sing()

# 调用静态属性和方法，可以使用 类名.属性    类名.方法名
print(A.name)
A.run()
A.sing(a)


#############调用的练习##########
