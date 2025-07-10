a=input("Enter email address: ")
b=a.find("@")
if b:
    if a[-4:]==".com":
        print("Valid email address")
    else:
        print("Invalid email address.")
else:
    print("Invalid email address.")
