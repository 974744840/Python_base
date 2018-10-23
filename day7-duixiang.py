# ###私有属性####私有属性不能在除了本类之外使用
# class Teacher:
#     sex=''
#     def __init__(self,name,age):
#         self.__name=name
#         if age>=18 and age<=40:     #如果要给私有属性加限制条件，那么条件里的属性不能带‘__’才可以通过
#             self.__age=age
#         else:
#             print('年龄不合法')
#             self.__age=0
#     def display(self):
#         print('姓名：',self.__name,'年龄：',self.__age)
#     def __AA(self):
#
#
#
# a=Teacher('小黑',18)
# a.display()
# a.__AA('男')
# class Book2:
#     title=''
#     page=0
#     def __init__(self,title,page=200):
#         self.title=title
#         if page>=200:
#             self.page = page
#         else:print('错误！')
#
#     def setTitle(self,title):
#         print('名称：',self.title)
#     def setPage(self,page=200):
#         if page>=200:
#             self.page = page
#         else:print('错误！')
#
#
#     def getTitle(self):
#         return self.title
#     def getPage(self):
#         return self.page
#     def detail(self):
#         print('名称：',self.title,'页数：',self.page)
#
# a=Book2('Java',)
# a.detail()
# a.setTitle('Python')
# a.setPage(300)
# print(a.getPage(),a.getTitle())
# ###########继承练习
# class grfather:
#      a1=2000
#      print(a1)
# class father(grfather):
#      a=1000
#      print(a)
# class me(father):
#      a2=500
#      print(a2)
# a=me()
# print(a.a1+a.a+a.a2)
#
# class Aniaml:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#     def info(self):
#         print('名字:',self.name,'颜色：',self.color)
# class Dog(Aniaml):
#     def work(self,li):
#         return li
#         print('看门...')
# class Cat(Aniaml):
#     def work(self,li):
#         return li
#         print('抓老鼠...')
#
# tom=Cat('小黑','彩色')
# tom.info()
# print(tom.work('吃狗粮！'))
#
# dg=Dog('小彩','红色')
# dg.info()
# print(dg.work('吃吃吃！'))
# #######作业###########
# 1、
# class Person:
#     def __init__(self):
#         print('父类构造！')
#     def eat(self):
#         print('我是super父类eat方法')
#     def sleep(self):
#         print('我是super父类sleep方法！')
#     def work(self):
#         print('我是super父类work方法！')
#
# class Student(Person):
#      def eat(self):
#          print('我是Student重写后的eat方法！')
#      def sleep(self):
#          print('我是Student重写后的sleep方法！')
#      def work(self):
#          print('我是Student重写后的sleep方法！')
#
#
# class Teacher(Person):
#     def eat(self):
#         print('我是Teacher重写后的eat方法！')
#
#     def sleep(self):
#         print('我是Teacher重写后的sleep方法！')
#
#     def work(self):
#         print('我是Teacher重写后的sleep方法！')
# a=Student()
# a.eat()
# a.sleep()
# a.work()
# super(Student,a).eat()
# b=Teacher()
# b.eat()
# b.sleep()
# b.work()
# super(Teacher,b).eat()
#
# 2、
# class Instrument:
#     def paly(self):
#         print('乐器演奏！')
# class Piano(Instrument):
#     def paly(self):
#         print('钢琴演奏！')
# class Violin(Instrument):
#     def paly(self):
#         print('小提琴演奏！')
# a=Instrument()
# a.paly()
# b=Piano()
# b.paly()
# c=Violin()
# c.paly()
#
# 3、递归
# nterms= int(input('需要几项？'))
# n1=0         #第一项
# n2=1         #第二项
# count=2       #进行计数，刚开始本来就是两项
#
# if nterms <=0:                #如果输入的项小于 0 那么执行输出提示输出正确的数
#     print('请输入一个正数。')
# elif nterms==1:               #如果输入的项等于 1  那么输出 n1 第一项
#     print('斐波那契数列：')
#     print(n1)
# else:                         #如果输入的项大于2，也就是除了上面两种选择
#     print('斐波那契数列：')
#     print(n1,',',n2,end=',')   #输出显示前两项  0 ，1
#     while count< nterms:      #利用循环，输出所有，先判断输入的项数是否大于现在已有两项，也就是输入 多少减去count，就等于要循环的次数，和161行，count+=1配合使用。
#         nth=n1+n2              #先把前两项加起来 == 第三项
#         print(nth,end=',')    #显示输出第三项  不换行  接着后面的输出
#         n1=n2                 #将第二项给了第一项
#         n2=nth                 #将前两项的和给了第二项  ，如此循环到下一圈
#         count+=1
# 理解：利用原始数  0 和 1  ，和while循环对的项数的限制，  除了第一圈把第三个数直接相加输出，后面的都是将该输出数的前两项赋给 第一第二 项利用循环算出相对位置的第三项
#
#
# 冒泡算法：原理是有n个数，第一轮循环执行n-1轮个循环 ，第二轮
# def maopao(nums):                    #创建冒泡方法
#     for i in range(len(nums)-1):     #控制最外轮的循环
#         for j in range(len(nums)-i-1):  #-i-1 等于原本的长度
#             if nums[j]>nums[j+1]:
#                 nums[j],nums[j+1]=nums[j+1],nums[j]
#     return nums
# nums=[55,52,12.2,38,19.5,99.9]
# print(maopao(nums))
#
class Teacher:
    def __init__(self,name,school):
        self.name=name
        self.school=school
    def giveLession(self):
        print('教学授课')
        print('布置作业')
    def info(self):
        print('我是',self.school,'的',self.name)

class JavaTeacher(Teacher):
    def __init__(self,name,school,id):
        self.name=name
        self.school=school
        self.id=id
    def info(self):
        print('我是',self.school,'的',self.name,'我的id:',self.id)
    def giveLession(self):
        print('打开eclipse')
        super().giveLession()
class HtmlTeacher(Teacher):
    def giveLession(self):
        print('打开Dreamweaver')
        super().giveLession()
#多态的精髓所在！！！！：传入父类名称，调用父类方法，再在下方创建各子类的对象，子类对象直接调用这个方法，结果就是
#传入哪个子类的对象，输出子类里面的对象！也就是在同一个机器输入不同的元素出来不同的结果，机器就相当于下面新建的对象，
#元素是各子类的子类对象
def duotai(Teacher):
    Teacher.info()
    Teacher.giveLession()

Java=JavaTeacher('张三','北京分校',10)
# Java.info()
# Java.giveLession()
Html=HtmlTeacher('李四','山西分校')
# Html.info()
# Html.giveLession()
duotai(Java)
duotai(Html)
# 整个程序中，个人信息是不一样的，授课是不一样。所以个人信息用父类构造方法创建，子类默认继承；接下来子类对象直接使用即可。
#                                                 而授课方法是内容不同，所以在子类中重写并用super超父类调用父类的方法
#                                                 最后显示过程中子类默认继承父类的显示方法，直接调用使用。子类再调用子类中
#                                                 重写的方法，所以直接显示子类要求输出的内容
#                 ##其目的：就是利用父类的继承(构造方法 和 info函数)、子类继承父类后的重写
#
