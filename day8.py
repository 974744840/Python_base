####作业########
#1、
import abc
class Pet(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getName(self,name):
        self.name=name
    def getAge(self):
        pass
    def getSex(self):
        pass
    def diaplay(self):
        print('姓名：',self.name,'年龄：',self.age,'性别：',self.sex)
# class QQ(Pet):
#     def getName(self,name):
#         self.name=name
#     def getAge(self,age):
#         self.age=age
#     def getSex(self,sex):
#         self.sex=sex
# a=QQ()
# a.getName('花花')
# a.getAge(10)
# a.getSex('男')
# a.diaplay()
# class Rabbit(Pet):
#     def getName(self,name):
#         self.name=name
#     def getAge(self,age):
#         self.age=age
#     def getSex(self,sex):
#         self.sex=sex
#     def getFood(self,food):
#         self.food=food
#     def diaplay(self):
#         print('姓名：',self.name,'年龄：',self.age,'性别：',self.sex,'兔子喜欢的食物：',self.food)
# b=Rabbit()
# b.getName('旭旭')
# b.getAge(10)
# b.getSex('女')
# b.getFood('肉！')
# b.diaplay()

#2、
# class Animal:
#     def eat(self):
#         pass
#     def sleep(self):
#         print('睡觉')
# class Rabbit(Animal):
#     def eat(self):
#         print('兔子喜欢吃肉！')
# class Tiger(Animal):
#     def eat(self):
#         print('老虎喜欢吃草！')
# class Text(Animal):
#     a = Rabbit()
#     b = Tiger()
#     a.eat()
#     a.sleep()
#     b.eat()
#     b.sleep()

#3、
# class Transport:
#     def __init__(self,type,color,pic):
#         self.type=type
#         self.color=color
#         self.pic=pic
#     def go(self):
#         print('启动！')
#     def stop(self):
#         print('停止！')
# class Bus(Transport):
#     def __init__(self,type,color,pic,pop,way):
#         self.type=type
#         self.color=color
#         self.pic=pic
#         self.pop=pop
#         self.way=way
#     def go(self):
#         print('公交车启动！')
#     def stop(self):
#         print('公交车停止！')
# class Freight(Transport):
#     def __init__(self,type,color,pic,huo,mil):
#         self.type=type
#         self.color=color
#         self.pic=pic
#         self.huo=huo
#         self.mil=mil
#     def go(self):
#         print('火车载着',self.huo,'吨货启动了！')
#     def stop(self):
#         print('货车形式了',self.mil,'里程之后到达了目的地开始卸货')
# class Text(Transport):
#     a=Bus('中巴','白色','￥：100100100','100人','长城--天安门')
#     b=Freight('半掉卡车','黑色','￥20000000',500,10000)
#     a.go()
#     a.stop()
#     b.go()
#     b.stop()

#4、
# import abc
# class riding(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def money(this):
#         pass
# class busC(riding):
#     def money(self):
#         print('滴！滴！公交卡')
# class stuC(riding):
#     def money(self):
#         print('滴！滴！学生卡')
# class oldC(riding):
#     def money(self):
#         print('滴！滴！老年卡')
# class text:
#     a=busC()
#     b=stuC()
#     c=oldC()
#     a.money()
#     b.money()
#     c.money()







