import shooping.menu
#用户类
class adm:
    def pri(self):
        print('———————————————————客户信息管理———————————————————')
        print('################################################')
        print('              1.显示所有客户信息')
        print('              2.添加客户信息')
        print('              3.修改客户信息')
        print('              4.查询客户信息')
    def choo1(self):
        choo11=int(input('请输入数字选择(或输入0返回上一层)：'))
        amd_show = show1_4()
        if choo11 == 1:
            print('################################################')  # 链接点
            amd_show.show1()
            shooping.menu.menu.menu(self)
            shooping.menu.menu.choo(self)
        elif choo11 == 2:
            print('################################################')  # 链接点
            amd_show.show2()
            shooping.menu.menu.menu(self)
            shooping.menu.menu.choo(self)
        elif choo11 == 3:
            print('################################################')  # 链接点
            amd_show.show3()
            shooping.menu.menu.menu(self)
            shooping.menu.menu.choo(self)
        elif choo11 == 4:
            print('################################################')  # 链接点
            amd_show.show4()
            shooping.menu.menu.menu(self)
            shooping.menu.menu.choo(self)
        elif choo11 == 0:
            shooping.menu.menu.menu(self)
            shooping.menu.menu.choo(self)
        else:
            print('请输入正确的')
####客户存储区####
kh_ztai=[['会员号','生日','积分']]
kh_xinxi=[[1623,'06.06',5000],[1545,'10.27',2000]]
####客户信息操作区####
class show1_4:
    ###显示客户信息方法
    def show1(self):
        print('鑫鑫在线购物系统>客户信息管理>显示所有客户信息')
        for i in range(0,len(kh_ztai)):
            print(kh_ztai[i])
        for i in range(0, len(kh_xinxi)):
            print( kh_xinxi[i])
    ###添加客户信息方法
    def show2(self):
        sh = []
        print('鑫鑫在线购物系统>客户信息管理>添加客户信息')
        ###索引已存在会员号########
        sh2_1 = str(input('请输入4位数会员号：'))
        if len(sh2_1) == 4:
            sh2_2 = str(input('请输入生日：'))  # sh2_2是月 sh2_2_1是日
            sh2_3 = int(input('请输入积分：'))
            if sh2_3 > 0:
                sh.append(sh2_1)
                sh.append(sh2_2)
                sh.append(sh2_3)
                print('新会员添加成功！')
            else:
                print('积分输入错误！')
        else:
            print('会员号输入错误！')
        kh_xinxi.append(sh)
    #修改客户信息方法
    def show3(self):
        print('修改还在开发中！')
    #查询客户信息方法
    def show4(self):
        print('索引还在开发中')


