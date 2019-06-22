class Turtle:
    def __init__(self,x):
        self.num = x

class Fish:
    def __init__(self,y):
        self.num = y

class Pool:
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
    def print_num(self):
        print("池子里总共有%d 只乌龟，%d条鱼" % (self.turtle.num,self.fish.num))

pool = Pool(10,20)
pool.print_num()
