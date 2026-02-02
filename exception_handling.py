try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("b is not defined",b)


