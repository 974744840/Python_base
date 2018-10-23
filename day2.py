# year=int(input('年份'))
# if year%100==0 or year%4==0 and year%100!=0:
#     print("闰年")


# pop=input('请输入身份：')
#
# if pop=='卫校学生' or pop=='卫校老师' or pop=='小胖女朋友':
#     print('可以进入学校！')
# else:
#     print('不能进入！')

# pp=input('你是什么身份？')
# pa=input('你是？')
# if pp=='狗' or pp=='日本人' or pa=='日本人' or pa=='狗':
#     print('不可以进入！')
# else:
#     print('可以进入！')

# cs=50;
# if 100>=cs>=90:
#     print('优秀')
# if 90>cs>=85:
#         print('良好')
# if 85>cs>=60:
#         print('及格')
# if cs<60:
#         print('不及格')

# gc=input('请输入工资：')
# a=300
# b=500
# c=3500
# zz=int(gc)-int(a)-int(b)-int(c)
# if 0<=zz and zz<1500:
#     print('最终交税：',zz*0.03)
# elif 1500<=zz and zz<4500:
#     print('最终交税：',zz*0.1-105)
# elif 4500<=zz and zz<9000:
#     print('最终交税：',zz* 0.2-555)
# elif 9000<=zz and zz<35000:
#     print('最终交税：',zz*0.25-1005)
# elif 35000<=zz and zz<55000:
#     print('最终交税：',zz*0.3-2755)
# elif 55000<=zz and zz<80000:
#     print('最终交税：',zz*0.35-5505)
# else:
#     print('最终交税：',zz*0.45-13505)
########
# if zz<=1500:
#      print('最终交税：', zz * 0.03)
# else:
#     if 1500<zz<4500:
#         print('最终交税：', zz * 0.1 - 105)
#     else:
#         if 4500<zz and zz<9000:
#             print('最终交税：', zz * 0.2 - 555)
#         else:
#             if 9000<zz and zz<35000:
#                 print('最终交税：', zz * 0.25 - 1005)
#             else:
#                 if 35000<zz and zz<55000:
#                     print('最终交税：', zz * 0.3 - 2755)
#                 else:
#                      if 55000<zz and zz<80000:
#                          print('最终交税：', zz * 0.35 - 5505)
#                      else:
#                          print('最终交税：', zz * 0.45 - 13505)
#


# ------------------------------作业-------------------------------
# 1. A=1  B=2   C=3    换完： A=3  B=1   C=2
# A=1
# B=2
# C=3
# D=0
# E=0
#
E=B
D=A
A=C
B=D
C=E
print(A,B,C)

# 2.张三为他的手机设定了自动拨号
# 按1：拨爸爸的号
# 按2：拨妈妈的号
# 按3：拨爷爷的号
# 按4：拨奶奶的号

bh=input('请输入编号：')
if int(bh)==1:
    print('拨爸爸的号')
elif int(bh)==2:
    print('拨妈妈的号')
elif int(bh)==3:
    print('拨爷爷的号')
elif int(bh)==4:
    print('拨奶奶的号')
else:
       print('输入错误！')

# 3.输入赵本山的考试成绩，显示所获奖励
# 成绩==100分，爸爸给他买辆车
# 成绩>=90分，妈妈给他买MP4
# 90分>成绩>=60分，妈妈给他买本参考书
# 成绩<60分，什么都不

a3=input('输入考试成绩')
if int(a3)==100:
    print('买辆车！')
elif int(a3)>=90:
    print('买MP4!')
elif int(a3)>=60:
    print('买书！')
elif int(a3)<60:
    print('什么也不买！')

# 4.判断用户名和密码是否正确
#  控制台：
#   请输入用户名：
#   请输入密码：
#   提示： 登录成功  失败

a4=input('请输入用户名：')
a44=input('请输入密码：')
if (str(a4)=='admin' and int(a44) ==123):
    print('登陆成功！')
else:
    if (str(a4)=='root' and str(a44) =='root'):
       print('登陆成功！')
    else:
       print('登陆失败！')

# 5.	输入一个四位数的数字判断出这个数字：千位   百位  十位  个位的数字并输出
#   提示：算术运算符

a5=input('请输入一个四位数：')
a5=str(a5)
lens=len(a5)

print('个位数是：'+a5[lens-1:lens])
print('十位数是：'+a5[lens-2:lens-1])
print('百位数是：'+a5[lens-3:lens-2])
print('千位数是：'+a5[lens-4:lens-3])

# 6.银行提供整存整取定期储蓄业务，分为一年  、 两年 、三年到期可以本息一起支取
# 存期  	年利息
# 一年	     2.25%
# 两年	     2.7%
# 三年	     3.6%

a6=input('请输入本金：')
a6=float(a6)
o=a6+a6*0.0225
t=a6+a6*0.027
s=a6+a6*0.036
print('存一年后的本息是：',o)
print('存一年后的本息是：',t)
print('存一年后的本息是：',s)

# 7.

a7=input('请输入出行月份1-12：')
a7=int(a7)
if(10<=a7<=12 or 1<=a7<=4):
    b2 = input('请问您旺季选择头等舱还是经济舱？头等输入 1 经济输入 2 :')
    b2=int(b2)
    if(b2==1):
        b2=5000*0.9
        print('机票为：',b2)
    else:
        b2=5000*0.6
        print('机票为：',b2)

else:
    b1=input('请问您淡季选择头等舱还是经济舱？头等输入1经济输入2:')
    b1=int(b1)
    if(b1==1):
        b2=5000*0.5
        print('机票为：',b2)
    else:
        b2=5000*0.4
        print('机票为：',b2)

# 8
print(' ---------------------------欢迎进入某某电子商城后台系统-----------------')
yh='admin'
mi='123'
a1=input('请输入用户名：')
a2=input('请输入密码：')
if(a1==yh and mi==a2):
    print('提示：登陆成功....')
    print('1.	添加商品：')
    print('2.	查询商品：')
    print('3.	管理商品：')
    b1=input('请选择操作：')
    if(b1=='1'):
        print('请输入：')
        print('商品名称：')
        print('商品价格：')
        print('商品数量：')
    else:
        if(b1=='2'):
            print('正在执行查询商品...')
        else:
            (b1=='3')
            print('正在执行管理商品...')
else:
    print('用户名或密码错误！')


