a=open("dilip1.txt","rb")
#g=input("please enter your name: ")
print(a.read(43))
print(a.tell())
print(a.seek(1,2))

a.close()