n=int(input("Enter a number: "))
for i in range(1,(n+1)):
    if (i%3==0 and i%5==0):
        print("Fizzbuzz")
    elif (i%3==0 and i%5!=0):
        print("Fizz") 
    elif (i%3!=0 and i%5==0):
        print("Buzz") 
    else:
        print(i)