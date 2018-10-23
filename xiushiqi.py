user_list ={'name': 'admin', 'pwd': '123'}
client_dic = {'username': None, 'pwd': None}
def auth_func(func):
    def wrapper():
        if client_dic['username']!=None:
            res = func()
            return res
        else:
            username = input('用户名:').strip()
            passwd = input('密码:').strip()
            if username == user_list['name'] and passwd == user_list['pwd']:
                client_dic['username'] = user_list['name']
                client_dic['pwd'] = user_list['pwd']
                res = func()
                return res
            else:
                print('用户名或者密码错误!')
    return wrapper
@auth_func
def f1():
    print("登陆成功!功能1")
@auth_func
def f2():
    print('登陆成功!功能2')
@auth_func
def f3():
    print('登陆成功!功能3')
f1()
f2()
f3()