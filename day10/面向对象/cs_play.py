# Author:xqkang
# Date:2020/10/21 下午8:00
class cs_play():
    def __init__(self, name, role, weapon, life_value=100, money=1500):
        '''
            构造函数：
            在实例化时做一些类的初始化的工作
        '''
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def got_shot(self):
        print("ah.....,I got shot...")
    def buy_gun(self,gun_name):
        print("%s ,just buy %s" % (self.name, gun_name))

r1 = cs_play('kxq','police','AK47')
r1.buy_gun("AK47")

