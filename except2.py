try:
    a=open("dilip3.txt","r")
    a.close()
except FileNotFoundError:
    print("file not found")
finally:
    pass