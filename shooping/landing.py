import shooping.menu
#登陆界面
class landin:
    #显示页面
    def pir(self):
        print('———————————————————欢迎使用鑫鑫在线购物系统———————————————————')
        print('                       1.登陆系统 ')
        print('                       2.退出')
        print('##########################################################')
    #登陆函数
    def land(self):
        cho = int(input('请输入数字选择：'))
        while True:
            if cho == 1:
                adm = input('请输入用户名：')
                paw = input('请输入密码：')
                if adm == 'admin' and paw == '0000':
                    shooping.menu.menu.menu(self)
                    shooping.menu.menu.choo(self)
                else:
                    print('输入用户或密码错误！')
                    print('#####################重新输入#########################')
            elif cho == 2:
                print('######退出系统！#######')
                quit()
            else:
                print('请输入正确数字选择！')



