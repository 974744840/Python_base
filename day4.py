# str='aaa@126.com'
# if(str.find('.')==-1 or (str.find('@'))==-1):
#     print('错误！')
# elif(str.find('.')>(str.find('@'))):
#     if((str.find('@'))==0):
#         print('错误！')
#     else:print('正确！')
# else:print('错误！')

# str='guorongxin.by'
# print(str[:-3])
# if(str[:-3].isalpha())==True:
#    if print(str[-3:])=='.by':
#        print('正确！')

# num=['1','2','4','5','6']
# mark.join(num)

#############作业#####################
#1.验证内容：6~18个字符，可使用字母、数字、下划线，需以字母开头
# li='gu97474484__0@126.com'
# print( li[:1])  #截取第一个字母
# print(li[0:-8])  #截取@前面所有字母
# s.isalnum() // 方法检测字符串是否由字母和数字组成。
# s.isalpha() // 是否全是字母，并至少有一个字符
# a=input('请输入注册邮箱：')
# if(6<len(a[0:-8])<18 and a[:1]).isalpha():  #检查长度和首字母？
#     if(a[0:-8].isalnum()==True):                    #判断是否由数字和字母组成？
#         print('正确！')
#     else:
#         a = a.count('_')
#         if a >= 1:
#             print('正确！')
#         else:
#             print('错误！')
# else:print('错误！')

###2.输入日期判断日期格式：1999-12-12

# a=input('请输入日期格式：')
# b1=int(a[0:4])
# b2=str(a[4:5])
# b3=str(a[5:7])
# b4=str(a[7:8])
# b5=int(a[8:10])
#
# if(2000<b1<3000 and( b1//400!=0 or b1/4!=0 and b1/100==0)):
#     if(b2=='-'):
#         if(b3=='01' or b3=='03' or b3=='05' or b3=='07' or b3=='08' or b3=='10' or b3=='12'):
#             if(b4=='-'):
#                 if(1<=b5<=31):
#                     print('正确！')
#                 else:print('错误！')
#             else:print('错误！')
#         else:
#             if(b3=='4' or b3=='6' or b3=='9' or b3=='11'):
#                 if (b4 == '-'):
#                     if (1 <= b5 <= 30):
#                         print('正确！')
#                     else:print('错误！')
#                 else:
#                     print('错误！')
#             else:
#                 if(b3=='2'):
#                     if(1<=b4<=29):
#                         print('正确！')
#     else:print('错误！')
# else:
#     if (b3 == '2'):
#         if (1 <= b4 <= 29):
#             print('正确！')

#3.定义一个长度为5的整型集合，循环输入5个整数，存储到集合中。
# 然后将输入一个整数，查找此整数， 找到 输出下标，没找到给出提示。
#
# a=[]
# for i in range(0,5):
#     b = int(input('请输入五位整数：'))
#     a.append(b)
#     print(a)
# c=int(input('请输入要查找的数：'))
# if c in a:
#     print(a.index(c))
# else:print('没找到！')

#4.骑士飞行棋
#地图布置
map=['■'*140]
print(map)
#随机骰子
import random
num= int((random.randint(1, 6)))  #随机产生1-6
print('摇到骰子：',num)
print(map.index(4))


