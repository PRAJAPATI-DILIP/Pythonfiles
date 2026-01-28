class student:
    def details(self ,name,age,rollno ):
        self.name=name
        self.age=age
        self.__rollno=rollno

name=input("please enter your name: ")
age=input("please enter your age: ")
rollno=input("please enter your roll no: ")

p1=student()
p1.details(name,age,rollno)
print(p1.name)
print(p1.age)
print(p1.__rollno)

