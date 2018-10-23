#####异常######
# try:
#     arr=[1,2,2,3,]
#     print(arr[2])
#     i=10
#     print(i)
# except:
#     print('捕捉异常 处理完毕')
# else:
#     print('没有异常出现')
try:
    f=open('input.txt',encoding='utf-8')
    try:
        while True:
            content=f.readline()
            if len(content)==0:
                break
            print(content)
    except:
        print('捕获到异常')
    finally:
        f.close()
        print('关闭文件')
except:
    print('异常：没有这个文件')
