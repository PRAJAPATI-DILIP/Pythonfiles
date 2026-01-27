#polymorphism means "many forms",
# programming it refers to methods/functions/operators
# with the same name that can be executed on many objects or classes.

#Function Polymorphism
#Same function works with different data types.
#Example: len() works for strings, lists, tuples, etc.
#Operator Polymorphism
# + adds numbers, concatenates strings, joins lists.


'''a= "welcome to python playlist"
b=[1,3,4,6,8,9]
c=(8,9,7,6,4,3,1)
print(len(a))
print(len(b))
print(len(c))
   OUTPUT
26
6
7'''

class shape:
    def area(self):
        pass
class rectangle(shape):
    def area(self):
        print("area of rectangle")
class square(shape):
    def area(self):
        print("area of square")
p1=shape()
Areas=[rectangle(),square()]
for a in Areas:
    a.area()

