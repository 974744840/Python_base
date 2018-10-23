import shooping.adm
#主菜单类
class menu:
    def menu(self):
        print('———————————————————主菜单———————————————————')
        print('###########################################')
        print('                1.客户信息管理')
        print('                2.购物结算')
        print('                3.真情回馈')
        print('                4.注销')

    def choo(self):
        import shooping.landing
        import shooping.shoop
        choo1=int(input('请输入数字选择(或输入0返回上一层)：'))
        while True:
            if choo1==1:
                print('######################################')
                print('进入客户信息管理')  #链接点
                shooping.adm.adm.pri(self)
                shooping.adm.adm.choo1(self)
                break
            elif choo1==2:
                print('######################################')
                print('进入购物结算')   #链接点
                shooping.shoop.shoop1.shangp(self)
                shooping.shoop.shoop1.pri_pic(self)
                break
            elif choo1==3:
                print('######################################')
                print('该功能还在开发中！') #链接点
                shooping.landing.landin.pir(self)
                shooping.landing.landin.land(self)
            elif choo1==4:
                print('######################################')
                shooping.landing.landin.pir(self)
                shooping.landing.landin.land(self)
            elif choo1==0:
                print('######################################')
                shooping.landing.landin.pir(self)
                shooping.landing.landin.land(self)
            else:
                print('请输入正确的')


