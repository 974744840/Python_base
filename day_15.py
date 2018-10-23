#########匿名函数#######
#普通函数
def f1(x):
    return x+1
def f2(x,y):
    return x*y
print(f1(10))
print(f2(2,3))
# #匿名函数
f3=lambda x:x+1     #匿名函数实现上面f1的x+1
print(f3(1))
f4=lambda x,y:x*y   #匿名函数实现上面f2的x和y相乘
print(f4(2,3))
# 理解:匿名函数即为一些简单的运算简单化设计

##########高阶函数#########
list1=[1,2,3,4,5]
# 题目:例表中数字乘以*2输出
#普通方法
def f1(arr):
    rs=[]
    for i in arr:
        rs.append(i*2)
    return rs
print(f1(list1))
#高阶方法
########map########
print("--------map--------")
def  add(x):
    return  x+1
print('list:',list(map(add,list1)))
#这个是将list1里的数字逐个进行add方法,最后放到list
print(list(map(lambda a:a+3,list1)))
# 这个是套了一个匿名函数,从而省去了新建add方法,直接使用
##########filter#########
print('-------filter筛选序列----------')
list3=range(100,500)
print(list3)  #==range(100, 500)
def sx(a):
    for i in list3:
        if i%3==0 and i%5==0:
            return i
##在定义函数中,return的返回值不一定非是传入的参数,但是只要有返回值,就需要有参数.
print(list(filter(sx,list3)))

# 1.列表推导式
list1= [  i  for  i in range(1,11)   ]
print(list1)

list2= [  i  for  i in range(1,11)   if i%2==0 ]
print(list2)

list3= [  i+10  for  i in range(1,11)   if i%2==0 ]
print(list3)

def f(x):
    return  x*x
list4= [  f(i)  for  i in range(1,11)   if i%2==0 ]
print(list4)

list5= [ i*k  for  i in range(1,11)   for  k in range(1,11) ]
print(list5)

# 2.字典
# k 和 v 互换
dict={"a":"aaaa","b":"bbbb","c":"cccc"}

dc= { i  for  i in dict}
print(dc)

dc= { v:k  for  k,v in dict.items()}
print(dc)

# 3.集合
set1= { i  for  i in range(1,11)   if i%2==0 }
print(set1)
