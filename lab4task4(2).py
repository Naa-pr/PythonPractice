a=float(input("Enter Fatin's age: "))
b=float(input("Enter Adian's age: "))
c=float(input("Enter Jobayer's age: "))
if a>b and a>c:
    print("Fatin is oldest who is",a,"years old")
if b>a and b>c:
    print("Adian is oldest who is",b,"years old")
if c>b and c>a:
    print("Jobayer is oldest who is",c,"years old")
if a>b and a==c:
    print("Fatin  and Jobayer are the oldest who are",a,"years old")
if a==b and a>c:
    print("Fatin and Jobayer is oldest who is",a,"years old")
if a==b and a==c:
    print("Fatin Adian and Jobayer are oldest who are ",a,"years old")




