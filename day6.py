# class MyClass:  # 创建类，名为MyClass
#     i = 1234     # 定义对象的成员：实例变量，为什么叫实例变量？因为对象是类的实例
#     def f(self):  # 定义对象的成员：方法
#         return 'hello world'
# #----------下面的定格写------------#
# x=MyClass()            #创建MyClass中的对象，名为：x
# print('i属性:',x.i)   #对象调用属性再显示
# print('f方法：',x.f()) #对象调用方法再显示
#
# class Complex:       #创建类，名为Complex
#     def __init__(self,real,ima):  #创建构造方法，并给两个属性：real,ima
#         self.r=real                #属性赋值
#         self.i=ima                #属性赋值
# x=Complex(3.0,-4.5)        #创建对象，对象自动调用，并赋值
# print(x.r,x.i)               #显示输出

# class people:    #创建类
#     name=''       #创建属性
#     age=0
#     ti=0
#     __weight=0     #定义私有属性
#     def __init__(self,n,a,w,t):  #创建构造方法
#         self.name=n            #相当于java中this.name=name ,
#         self.age=a             #不过这个这里构造方法的变量和类的变量不能相同,
#         self.__weight=w        #作用：传递数据，不同的对象自动调用了构造方法后，必须进行赋值如：28行
#         self.ti=t
#     def speak(self):           #创建显示信息的方法
#         print("%s说:我%d岁,我%d斤重。"%(self.name,self.age,self.ti))    #  %s 是显示字符串   %d是显示int型 后面相对的
# #实例化类
# p=people('小郭',10,160,120)
# p.speak()

########继承##########
# class people:    #创建类
#     name=''       #创建属性
#     age=0
#     ti=0
#     __weight=0     #定义私有属性
#     def __init__(self,n,a,w,t):  #创建构造方法
#         self.name=n            #相当于java中this.name=name ,
#         self.age=a             #不过这个这里构造方法的变量和类的变量不能相同,
#         self.__weight=w        #作用：传递数据，不同的对象自动调用了构造方法后，必须进行赋值如：28行
#         self.ti=t
#     def speak(self):           #创建显示信息的方法
#         print("%s说:我%d岁,我%d斤重。"%(self.name,self.age,self.ti))    #  %s 是显示字符串   %d是显示int型 后面相对的
#
# class student(people):    #继承people父类
#     grade=''               #创建新的属性
#     def __init__(self,n,a,w,t,g):     #创建子类的构造方法，这里注意要加上子类新的属性和父类的所有属性，51行相同操作
#         people.__init__(self,n,a,w,t)    #调用父类的构造方法
#         self.grade=g
#     def speak(self):
#         print("%s说:我%d岁,我%d斤重,我%s年级了！"%(self.name,self.age,self.ti,self.grade))
#
# a=student('小安',20,500,120,'三年级')
# a.speak()

######方法重写###########有点不理解
# class Parent:               #创建父类
#     def myMethod(self):     #创建父类方法
#         print('父类！')
# class Child(Parent):  #定义子类并继承父类
#     def myMethod(self):  #创建子类方法  注：这里的方法名和父类中的一样，也就是重写
#         print('子类！')
# c=Child()    #子类对象，也叫实例
# c.myMethod()   #调用子类的重写方法
# super(Child,c).myMethod()  #用子类对象调用父类已被覆盖的方法
# print(super(Child,c).myMethod())

##########作业##############
#1、
# class jisuanji:
#     a=0
#     b=0
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return(self.a + self.b)
#     def sub(self):
#         return (self.a-self.b)
#     def mul(self):
#         return (self.a*self.b)
#     def div(self):
#         return (self.a/self.b)

# 2、
class student:
    name=''
    sex=''
    age=0
    cla=''
    def __init__(self,name,sex,age,cla):
        self.name=name
        self.sex=sex
        self.age=age
        self.cla=cla
    def setName(self,name):     #有  有
        return '姓名s：',name
    def setSex(self,sex):      #有  无
        print('性别s：',sex)

    def getAge(self):       #无  有
        return '年龄是：',self.age
    def getCla(self):   #无  无
        print('班级s：',self.cla)

    def display(self):    #所有信息
        print("%s个人信息：性别：%s 年龄： %d 班级：%s"%(self.name,self.sex,self.age,self.cla))
a=student('小郭','男',23,'三年级')
a.display()

a.setSex('男')    #有 有调用
print(a.setName('小红'))  #有 无 调用

print(a.getAge())    # 无 有 调用
a.getCla()          #无 无 调用


#3、
# class Person:
#     name=''
#     age=0
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def getName(self):
#         return '小黑'
#     def getAge(self):
#         return 18
#     def display(self):
#         print('姓名：',self.name,'年龄：',self.age)
# po=Person('小鑫',23)
# po.display()
# print(po.getName())
# print(po.getAge())


