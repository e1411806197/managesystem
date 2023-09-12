from enum import Enum
from system_txl import txl
from typing import Union
class sf_id(Enum):
    __type='身份id'
    """总管 管理员 普通成员  对应 0  1  2"""
    zg=0
    gly=1
    ptcy=2


class people(object):
    typing='成员基类'
    def __init__(self,name:str='aaa',age:int=23,sfz_number:str='222211121',phone:str='222',shenfen_id:sf_id=0):
        self.name=name
        self.age=age
        self.sfz_number=sfz_number
        self.phone=phone
        self.shenfen_id=shenfen_id

    def add(self):
        pass

    def remove(self):
        pass

    def change(self):
        pass

    def find(self):
        pass

    def sort(self):
        pass


class zfzr(people):
    __type='总负责人'
    __work='增删改差管理员相关信息以及创建删除通讯录'
    def __init__(self):
        super().__init__()
        self.gly_list=[]
        self.txl_list=[]

    def add(self):
        name=input('请输入管理员的姓名:')
        age = int(input('请输入管理员的年龄:'))
        sfz_number = input('请输入管理员的身份证号:')
        phone = input('请输入管理员的手机号:')
        sf_id = int(input('请输入管理员的身份:'))
        gh=input('请输入管理员的工号:')
        txl_id=input('请输入管理员管理的通讯录id')
        maxlenth = int(input('请输入通讯录的最大长度'))
        self.make_txl(txl_id, maxlenth)
        self.gly_list.append(gly(name,age,sfz_number,phone,sf_id,gh,txl_id,txl(txl_id,maxlenth)))



    def remove(self):
        number=input('请输入管理员的身份证号:')
        try:
            self.gly_list.remove([i for i in self.gly_list if i.sfz_number==number][0])
        except:
            print('查不到该人员的信息')


    def change(self):
        name=input('请输入修改管理员的姓名:')
        try:
            xg_gly=[i for i in self.gly_list if i.name==name][0]
            age = int(input('请输入修改管理员的年龄:'))
            sfz_number = input('请输入修改管理员的身份证号:')
            phone = input('请输入修改管理员的手机号:')
            sf_id = int(input('请输入修改管理员的身份:'))
            gh = input('请输入修改管理员的工号:')
            txl_id = input('请输入修改管理员管理的通讯录id')
            xg_gly.age=age
            xg_gly.sfz_number = sfz_number
            xg_gly.phone = phone
            xg_gly.shenfen_id = sf_id
            xg_gly.gh = gh
            xg_gly.txl_id = txl_id

        except:
            print('查不到该人员的信息')



    def find(self):
        name=input('请输入查询管理员的姓名:')
        try:
            gly=[i for i in self.gly_list if i.name==name][0]
            print('管理员的姓名为',gly.name)
            print('管理员的年龄为', gly.age)
            print('管理员的手机号为', gly.phone)
            print('管理员的工号为', gly.gh)

        except:
            print('查询不到此管理员信息')


    def perform_allgly(self):
        for i in self.gly_list:
            print('管理员的姓名为',i.name,'管理员的年龄为',i.age,'管理员的手机号为',i.phone,'管理员的工号为',i.gh)
    def sort(self):
        print('仅支持年龄与工号排序')
        content=input('请您输入要排序的信息')
        if content=='年龄':
            self.gly_list.sort(key=lambda x:x.age)
            self.perform_allgly()
            print('排序成功')

        elif content=='工号':
            self.gly_list.sort(key=lambda x:int(x.gh))
            self.perform_allgly()
            print('排序成功')

        else:
            print('此信息无法排序请重新输入')



    def make_txl(self,txl_id,maxlenth):

        self.txl_list.append(txl(maxlenth,txl_id))



    def remove_txl(self):
        txl_id=int(input('请输入删除通讯录id'))
        try:
            self.txl_list.remove([i for i in self.txl_list if i.txl_id==txl_id][0])
            print('删除成功')
        except:
            print('查询失败')


class gly(people):
    __type='管理员'
    __work='增删改查普通人员信息'
    def __init__(self,name,age,sfz_number,phone,sf_id,gh,txl_id:int,txl:txl):
        """需要添加管理员的工号  管理的通讯录的id"""
        super().__init__(name,age,sfz_number,phone,sf_id)
        self.gh=gh
        self.txl_id=txl_id
        self.txl=txl


    def add(self):
        if len(self.txl.cunchu)==self.txl.maxlenth:
            print('无法添加')
            return
        name = input('请输入普通成员的姓名:')
        age = int(input('请输入普通成员的年龄:'))
        sfz_number = input('请输入普通成员的身份证号:')
        phone = input('请输入普通成员的手机号:')
        sf_id = int(input('请输入普通成员的身份:'))
        self.txl.cunchu.append(ptry(name,age,sfz_number,phone,sf_id))


    def remove(self):
        name = input('请输入删除普通成员的姓名:')
        try:
            self.txl.cunchu.remove([i for i in self.txl.cunchu if i.name==name][0])
            print('删除成功')
        except:
            print('无法删除查询不到此人')

    def change(self):
        name=input('请输入修改普通成员的姓名:')
        try:
            change_people=[i for i in self.txl.cunchu if i.name==name][0]
            age = int(input('请输入普通成员的年龄:'))
            sfz_number = input('请输入普通成员的身份证号:')
            phone = input('请输入普通成员的手机号:')
            change_people.age=age
            change_people.sfz_number = sfz_number
            change_people.phone = phone
        except:
            print('没有此人,无法修改')

    def find(self):
        name=input('请输入查询普通成员的姓名:')
        try:
            find_people=[i for i in self.txl.cunchu if i.name==name][0]
            print('普通成员的姓名为', find_people.name)
            print('普通成员的年龄为', find_people.age)
            print('普通成员的手机号为', find_people.phone)
            print('普通成员的身份证为', find_people.sfz_number)
            print('普通成员的身份为', find_people.shenfen_id)
        except:
            print('查询不到此人')

    def perform_allgly(self):
        for i in self.txl.cunchu:
            print('普通成员的姓名为', i.name, '普通成员的年龄为', i.age, '普通成员的手机号为', i.phone, '普通成员的身份证号为',
                  i.sfz_number,'普通成员的身份为',i.shenfen_id)
    def sort(self):
        print('只支持年龄排序')
        content=input('请输入排序的信息:')
        if content=='年龄':
            self.txl.cunchu.sort(key=lambda x:x.age)
            self.perform_allgly()
        else:
            print('输入字段错误请重新输入')

class ptry(people):
    __type='普通人员'
    __work='修改查找本人的信息'
    def __init__(self,name,age,sfz_number,phone,sf_id):
        super().__init__(name,age,sfz_number,phone,sf_id)




if __name__ == '__main__':
    ss=[1,45,23,78]
    ss.sort()
    print(ss)



#