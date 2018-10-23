print("a", end='')
print("b")
age=20
type(age)
print(age)

a='郭荣鑫'
print(a)
type(a)

# 显示数字方法一：用逗号连接， 用%的 %f %s


#a1=input('本人颜值：')
#a2=input('同桌研制：')

#print(a1>a2,'本人比同桌漂亮')


mat=input('语文成绩：')
yx=input('数学成绩：')
print('可以获得奖励？',(int(mat)==100 or int(yx)==100 ) or int(mat)>85 and int(mat)>85)

mat=input('语文成绩：')
yx=input('数学成绩：')
print((int(mat)==100 or int(yx)==100 ) or int(mat)>85 and int(mat)>85)
che=input('有车吗？(请输入：Y或N):')
fang=input('有房吗？(请输入：Y或N):')
print ('晚上可以一起约会吗？',(str(che)=='Y' and str(fang)=='Y'))


hit=input('身高：')
eig=input('体重：')
print('买票？',int(hit)>=120 and int(eig)>=50   )

year=input('请输入年份：')

print('是否为闰年？',int(year)//400==0 or (int(year)/4==0 and int(year)/100!=0  ))