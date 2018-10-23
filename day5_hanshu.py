# count=0
# str='afdasfdafds'
# for i in str:
#     count+=1
# print(count)
#####函数，长度###
# def long (str):
#     count = 0
#     for i in str:
#         count += 1
#     return (count)
# cc=long('sfdafdafdsa')
# print(cc)

#获得某个字母在字符串的位置  abc    a  找到返回索引 0  没有：-1
# def getIndex(s,f):
#     if f in s:
#         index=0
#         for i in s:
#             if i==f:
#                 return index
#             else:
#                 index +=1
#     else:
#         return -1
# a=getIndex('abc','a')
# print(a)

# tup1 = ('Google', 'Runoob', 1997, 2000);
# tup2 = (1, 2, 3, 4, 5 );
# tup3 = "a", "b", "c", "d";   #  不需要括号也可以
# print(type(tup3))
# print(tup1[1])
# print(tup2[0:4])
# tup4=tup1+tup2
# print(tup4)
#
# print(len(tup1))
# def text1(sc,cou='java'):
#     print(cou,'得了：',sc,'分')
# a=text1(100)
# b=text1(60,'c++')
# print(b)
# print(a)
# def test3(x,*args):
#     print(x)
#     print(args)
#     print(args[0])
#
# test3(1,2,3,4)
# test3(1,*['a','b','c'])

##########作业##########
# 分析：1、书和状态列表 2、主界面 3、更改状态的方法 4、返回主界面的方法
print('————————欢迎进入借书系统！————————')
print('1、查看可借的书')
print('2、借书')
print('3、退出系统')
##############图书列表和图书状态################
book = ['盗墓笔记', '武动乾坤', '斗破苍穹', '大主宰', '斗罗大陆']
state=[' 没借走 ', ' 已借走 ', ' 没借走 ', ' 没借走 ', ' 没借走 ', ]
#########显示图书列表和状态的函数######
def show():
    for i in range(0, 5):
        print(book[i], state[i])
#########借书并修改状态方法########
def cho1():
    a = str(input('请输入书名：'))
    for i in state:
        i1 = book.index(a)
        if (state[i1] == ' 没借走 '):
            for k in book:
                if k == a:
                    state[i1] = '已借走'
                    print('操作成功！')
            break
        else:
            print('本书也被已借走')
        break
###########返回函数#########
def ret():
    re=int(input('输入0返回:'))
    if re==0:
        print('————————欢迎进入借书系统！————————')
        print('1、查看可借的书')
        print('2、借书')
        print('3、退出系统')

#######################选择界面方法#################
def cho():
    choose = int(input('请输入选择：'))
    if (choose == 1):  # 选择1
        show()
    elif (choose == 2):  # 选择2
        show()
        cho1()
    elif (choose == 3):  # 选择3
        quit()
# #################主函数开始################
while(True):
    cho()       #调用选择函数
    ret()



