class parent:
    def diet(self,name,time):
        self.name=name
        self.time=time

food1 = input("Enter the food name: ")
food2 = input("Enter the food time: ")

p1=parent()
p1.diet(food1,food2)
print(p1.name)
print(p1.time)

class child(parent):
    def diet1(self,name,time):
        self.name=name
        self.time=time

food1 = input("Enter the food name: ")
food2 = input("Enter the food time: ")

p2=child()
p2.diet1(food1,food2)
print(p2.name)
print(p2.time)
