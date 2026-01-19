a=int(input("enter a number1: "))
b=int(input("enter a number2: "))
c=input("Enter the operator for operation +,-,*,/ ")

if c=='+':
    print ("result", a+b)
elif c=="-":
    print ("result", a-b)
elif c=="*":
    print ("result", a*b)
elif c=="/":
    if b==0:
        print("Denominator never should be 0",)
    else:
        print("result", a/b)
else:
    print ("Incorrect operator")