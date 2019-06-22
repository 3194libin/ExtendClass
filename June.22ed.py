import random as r

class Fish:
    def fish(self):
        print("我是一条小鱼")
class GoldFish:
    def goldfish(self):
        print("我是一条金鱼")
class Carp:
    def carpfish(self):
        print("我是一条鳗鱼")
class Shark(Fish,GoldFish,Carp):
    pass

s = Shark()
s.carpfish()
s.fish()
s.goldfish()
