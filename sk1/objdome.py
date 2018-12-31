class UserModel:
    name=""
    age=0
    def __init__(self,name,age):
        UserModel.name=name
        UserModel.age=age

    def show(self):
        print(UserModel.name)
        print(UserModel.age)

    def setName(self,name):
        UserModel.name=name

    def getName(self):
        return UserModel.name

if __name__ == '__main__':
    user= UserModel("huangz",18)
    user.setName("yihui")


    user.show()

    print(user.getName())