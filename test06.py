#面向对象
class user:
    def __init__(self,a,b):
        print("a")
        print("b")


    def work(self):
        print("user work")


    def sayHi(self,word):
        print(word)


u=user("a","b")
u.work()
u.sayHi("huangz")
u.sayHi("wwwww")