#无参数无返回值
def d1():
    print('无返回值无参数')
#无参数有返回值
def d2():
    x=1
    return x
# 注:这种情况返回的值,必须要在本函数中进行定义
#有参数有返回值
def d3(x):  #返回参数和函数内定义的变量
    y=3
    return y,x
def d4(x,y):  #返回参数和返回值无关
    c=y*x
    return c
def d5(x):  #返回参数和返回值相同
    return x
#有参数，无返回值
def d6(x):          #这种无意义
    print('有参无反')
def d7(x,y):        #这种也有意义
    c=x*y
    print(c)





