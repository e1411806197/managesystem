from system_people import zfzr
class manage_system(object):
    __type='管理系统界面'
    def __init__(self):
        print('请先添加管理员再进入系统')
        self.zfzr=zfzr()

    def tkinter(self):
        print(manage_system.__type)
        print("-----------------------------")
        print('0.总管')
        print('1.管理员')
        print('2.退出')
        print('-----------------------------')
        self.first=input('请输入您的身份：')

    def zg_jm(self):
        print('总管界面')
        print("-----------------------------")
        print('1.添加管理员')
        print('2.删除管理员')
        print('3.修改管理员')
        print('4.查找管理员')
        print('5.管理员信息展示')
        print('6.管理员信息排序')
        print("-----------------------------")
        self.second=input('请输入总管您的选择:')



    def gly_jm(self):

        print('管理员界面')
        print("-----------------------------")
        print('1.添加普通成员')
        print('2.删除普通成员')
        print('3.修改普通成员')
        print('4.查找普通成员')
        print('5.普通成员信息展示')
        print('6.普通成员信息排序')
        print("-----------------------------")
        self.last=input('请输入管理员您的选择')

    def function(self):
        self.tkinter()
        if self.first=='0':
            self.zg_jm()
            if self.second=='1':
                self.zfzr.add()
                return self.function()
            elif self.second=='2':
                self.zfzr.remove()
                return self.function()
            elif self.second=='3':
                self.zfzr.change()
                return self.function()
            elif self.second=='4':
                self.zfzr.find()
                return self.function()
            elif self.second=='5':
                self.zfzr.perform_allgly()
                return self.function()
            elif self.second=='6':
               self.zfzr.sort()
               return self.function()
            else:
                print('输入错误')
                return self.function()
        elif self.first=='1':
            self.gh = input('请输入您的工号')
            try:
                self.current_gly=[i for i in self.zfzr.gly_list if i.gh==self.gh][0]
            except:
                print('查询不到')
                return self.function()
            self.gly_jm()
            if self.last=='1':
                self.current_gly.add()
                return self.function()
            elif self.last=='2':
                self.current_gly.remove()
                return self.function()
            elif self.last=='3':
                self.current_gly.change()
                return self.function()
            elif self.last=='4':
                self.current_gly.find()
                return self.function()
            elif self.last=='5':
                self.current_gly.perform_allgly()
                return self.function()
            elif self.last=='6':
                self.current_gly.sort()
                return self.function()
            else:
                print('输入错误')
                return self.function()
        elif self.first == '2':
            exit(200)
        else:
            print('输入不正确，请重新输入')
            return self.function()

    def boot_main(self):
        self.function()


if __name__ == '__main__':
    system=manage_system()
    system.boot_main()


