import os,sys,stat
import os.path
###文件基本操作
# pa='day8.py'    #相对路径
# pa1='g:/text'   #绝对路径
# print(os.path.abspath(pa))   #获取相对路径
# print(os.path.dirname(pa1))   #获取绝对路径
# print(os.path.basename(pa1))   #获取文件或文件名的名称
# print(os.path.split(pa))      #对文件或文件名进行分割
# ###获取文件基本信息
# print(os.path.getsize(pa))  #获取pa2文件的大小
# print(os.path.isdir(pa1))  #判断是否为文件夹
# print(os.path.isfile(pa))  #判断是否为文件
# print(os.path.isabs(pa1))  #判断是否为绝对路径
###文件和文件夹的创建和删除
# os.mkdir('aaa')        #创建相对文件aaa?
# os.mkdir('g:/a')       #创建绝对路径文件夹a
# os.makedirs('g:/a/g/b/a')   #逐个创建子文件夹
# os.rmdir('aaa')       #删除一个
# os.removedirs('g:/a/g/b/a')  #删除多个
# os.rename('aaa','bbb')    #重命名一个
# os.remove('g:/a.txt')      #删除单个文件
# print(os.listdir('d://'))  #获取目录中的列表


# pa='G:/python'
# print(os.path.dirname(pa))
# print(os.path.exists(os.path.dirname(pa)))
# open('G:/python/a.txt','w')


# 练习：
# 1、遍历一个目录列表，判断列表中的目录和文件，输出所有的文件名称和文件大小
# path = 'D:\\'
# for i in (os.listdir('D:\\')):
#     newPath = path+i
#     b = os.path.isfile(newPath)  #判断是否为文件
#     c = os.path.isdir(newPath)  #判断是否为文件夹
#     if b==True:
#         print('文件：', i, '大小', os.path.getsize(newPath))
# 2、创建文件 d:\doc\io.doc，首先我不知道目录是否存在，无则创建，有则创建新的
# p1='g:\\doc\\io.doc'
# a=os.path.dirname(p1)
# os.path.exists(a)
# if a==True:
#    print('已存在！')
# else:
#    os.makedirs(p1)
#    open(p1)

##文件读取，兼汉字
# a=open('a.txt',encoding='utf-8')
# while True:
#     str=a.read(1)
#     print(str,end='')
#     if str=='':
#         break

##文件写入，兼汉字
# b=open('a.txt','a+',encoding='utf-8')
# b.write("fdaff放大发达发达是")
###逐行输出
# f=open('text.txt','r+',encoding='utf-8')


###############作业###############
# 1、
# a=open('data.txt','w+',encoding='utf-8')
# a.write('小张 ')
# a.write('13888888888\n')
# a.write('小李 ')
# a.write('13999999999\n')
# a.write('小赵 ')
# a.write('13666666666\n')
# a.flush()
# a.close()
# b=open('data.txt',encoding='utf-8')
# str = b.read(2)
# print('姓名:', str)
# str1 = b.read(13)
# print('电话:', str1)
# str2=b.read(3)
# print('姓名:',str2)
# str3=b.read(12)
# print('电话:',str3)
# str4=b.read(3)
# print('姓名:',str4)
# str5=b.read(12)
# print('电话:',str5)
# b.flush()
# b.close()

# 2、
# path="G:\KEIL5"
# for i in os.walk(path):
#     print(i)
# def getAllfileAndDirPath(sourcePath):
#     if not os.path.exists(sourcePath):
#         return
#     listName = os.listdir(sourcePath)
#     for name in listName:
#         absPath = os.path.join(sourcePath,name)
#         if os.path.isfile(absPath):
#             print('filePath:%s' % absPath)
#         if os.path.isdir(absPath):
#             getAllfileAndDirPath(absPath)
#
# getAllfileAndDirPath(r'D:\Temp')
#3、
# a=open('input.txt','r',encoding='utf-8')
# arr=[]
# while True:
#     b=a.readline()
#     arr.append(b)
#     if b=='':
#         break
# print('1:',arr[0])
# print('2:',arr[1])
# print('3:',arr[2])
# print('4:',arr[3])
# 4、
# rootdir='G://siti'
# for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
#     print(os.walk(rootdir))
#     new_suffix = '.doc'
#     for filename in filenames:
#         if filename.endswith('.txt'):
#             name_without_suffix = filename[:-4]
#             os.rename(os.path.join(rootdir, filename), os.path.join(rootdir,name_without_suffix + new_suffix))





