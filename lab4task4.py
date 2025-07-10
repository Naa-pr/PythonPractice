a=float(input("Enter Fatin's age: "))
b=float(input("Enter Adian's age: "))
c=float(input("Enter Jobayer's age: "))
largest=a
verb="is"
name="Fatin"
if b>a:
    largest=b
    name="Adian"
    verb="is"
if c>largest:
    largest=c
    name="Jobayer"
    verb="is"
if largest==a and a==b:
    name="Fatim and Adian"
    verb="are"
if largest==a and a==c:
    name="Fatin and Jobayer"
    verb="are"
if largest==b and b==c:
    name="Adian and Jobayer"
    verb="are"
if largest==a and a==b and a==c:
    name="Fatin Adian and Jobayer"
    verb="are"
print(f'{name} {verb} the oldest who {verb} {largest} years old')
