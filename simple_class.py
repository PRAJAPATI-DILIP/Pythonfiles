#class simple:
#    def __init__(self,version):
#        self.version=version

#p1=simple(3.2)
#print(p1.version)
class prime:
    def check_prime(self, number):
        self.number =number
        for x in range(2,number):
            if number % x==0:
                print("Not Prime")
                break

            else:
                print("Prime")
                break
p1=prime()
p1.check_prime(int(input("Enter the number to check ")))



