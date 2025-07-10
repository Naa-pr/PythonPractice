a=int(input("Enter 1st integer :"))
b=int(input("Enter 2nd integer :"))
flag=input("Input must be either true or false")
if flag=="false":
    if a>0 and b<0:
        print("True")
    elif a<0 and b>0:
        print("True")
    else:
        print("False")
elif flag=="true":
    if a<0 and b<0:
        print("True")
    else:
        print("False")
else:
    print("False")
