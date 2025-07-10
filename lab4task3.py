a=float(input("Enter your score: "))
if a<=100 and a>=0:
    if a>=80:
        print("A+")
        print("Congratulations!")
    elif a>=75:
        print("A")
        print("Congratulations!")
    elif a>=70:
        print("A-")
        print("Congratulations!")
    elif a>=65:
        print("B")
        print("Congratulations!")
    elif a>=60:
        print("B-")
        print("Congratulations!")
    elif a>=55:
        print("C+")
        print("Congratulations!")
    elif a>=50:
        print("C+")
        print("Congratulations!")
    elif a>=45:
        print("C")
        print("Congratulations!")
    elif a>=40:
        print("D")
        print("Congratulations!")
    else:
        print("F")
        print("Congratulation")
else:
    print("Invalied Input")
