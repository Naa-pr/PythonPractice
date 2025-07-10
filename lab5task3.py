a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
c=float(input("Enter third number: "))
largest=a
if b>a:
    largest=b
if largest<c:
    largest=c
print("The largest number is ",largest)
