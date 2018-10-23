####  for 循环
# str='hello123456'
# c=0
# print(len(str))
# for i in str:
#     c+=1
# print(c)

####利用for循环输出偶数
# for i in range(1,101):
#     if i%2==0:
#        print(i)

# ###输出1-100 中偶数之和
# sum=0
# for i in range(1,101):
#     if i%2==0:
#         sum+=i
#         print(sum)

# 里面有几个a
# str='heallo12a34a45a'
# sum=0
# for i in str:
#     if i=='a':
#         sum+=1
# print(sum)
#####练习形状输出#####
# for i in range(1,5):
#     for j in range(1,5):
#         print('*',end='')
#     print()
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()

# for i in range(1,5):
#     for k in range(i, 4):  # 输出空格
#         print(" ", end="")
#     for j in range(1, i*2): #    输出星号
#         print("*",end='')
#     print()   #换行

#############################作业#########################
#1、空心正方形
# for i in range(1,5):
#     print('*', end='')
# print()
# for j in range(1,5):
#     if j==2 or j==3:
#         print(' ',end='')
#     else:
#         print('*',end='')
# print()
# for j in range(1,5):
#     if j==2 or j==3:
#         print(' ',end='')
#     else:
#         print('*',end='')
# print()
# for i in range(1,5):
#     print('*', end='')
# print()
#2、菱形 for
# for i in range(1,7):       #大循环控制行数
#     for k in range(i,7):   #这里的循环控制输出空格且，括号里左面的i是逐渐增大的，所以输出越来越少
#         print(' ',end='')
#     for j in range(1,i*2):  # 这里的循环控制星号输出，且括号右面越来越大  i*2控制输出单数星号
#         print('*',end='')
#     print()
#
# for i in range(1,7):
#     for n in range(1,i+2):   #输出
#         print(' ',end='')
#     for m in range(1,12-i*2):
#         print('*',end='')
#     print()
  ######菱形while########
# i=0
# j=0
# k=0
# n=0
# m=0
# while i<7:
#     while j < 7:
#         print('*', end='')
#         j += 1
#     i+=1

#3、检索出两个字符穿中相同的字母
# str1='asdff2'
# str2='sfs2ad'
# j=0
# for i in str1:
#     for j in str2:
#         if i==j:
#             print(i)

#5、求出100以内的质数  提示：约数只有1和本身
# count=0
# i=2
# for i in range(2,100):
#     j = 2
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

#4控制台输入5名的学生成绩，如果系统输入的参数为负数，说明操作者输入错误，
# 直接退出系统，如果输入参数正确就统计出他们5名学生的平均分
# sum=0
# for i in range(1,6):
#     a = int(input('请输入五个人的成绩:'))
#     sum+=a
#     if a<0:
#         print('输入错误！')
#     avg=sum/5
# print('平均成绩：',avg)

#6、模拟银行登录系统
# print('请插入银行卡...')
# print('银行卡读取完成')
# j=3
# for i in range(1,4):
#     j-=1
#     a=int(input('请输入密码：'))
#     if a!=123:
#         print('错误，请重新输入..')
#         print('剩余',j,'次')
#         if j==0:
#             print('如果第三次输入失败，告知银行卡已锁，请到柜台解锁')
#     else:
#         if a==123:
#             print('成功！')
#             break

#7、在综艺节目，有猜物品价格的节目
# print('欢迎参加节目，物品已经准备好！')
# import random
# a = int((random.randint(0, 100)))
# c=5
# for i in range(1,6):
#     c-=1
#     print(a)
#     b=int(input('请输入价格：'))
#     if a==b:
#         print('对了！')
#         break
#     elif b>a:
#         print('高了')
#         print('还有',c,'次机会')
#     elif b<a:
#         print('低了')
#         print('还有', c, '次机会')
# if c==4:
#     print('一次答对!奖励汽车')
# elif c==3:
#     print('二次答对!奖励冰箱')
# elif c==2:
#     print('三次答对!奖励热水壶')
# elif c==1:
#     print('四次答对!奖励水杯')
# elif c==0:
#     print('五次答对!奖励手机支架')











