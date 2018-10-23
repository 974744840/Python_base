
class shoop1:
    spp = [[1, 'addidas运动鞋', 880], [2, 'Nike运动鞋', 520], [3, 'addidasT恤', 380]]
    sp = []
    def shangp(self):
        a = """
        1:addidas运动鞋
        2:addidasT恤
        3:Nike运动鞋
        """
        print(a)
    def pri_pic(self):
        a=shoop1()
        while True:
            id = int(input('请输入商品编号：'))
            count = int(input('请输入商品数量：'))
            for i in a.spp:
                if id == i[0]:
                    sum = count * i[2]  # 总价
                    a.sp.append([i[1], i[2], count, sum])
                    YES_NO = input('是否继续？（Y/N）')
                    if YES_NO == 'y':
                        continue
                    elif YES_NO == 'n':
                        print("****************消费清单*****************")
                        print('物品        ', '单价   ', '个数    ', '金额')
                        sum = 0
                        for i in a.sp:
                            print(i[0], i[1], i[2], i[3])
                            sum = sum + i[3]
                        print("总金额：", sum)
            break






