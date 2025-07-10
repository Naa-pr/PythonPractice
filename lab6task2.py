a=input("Enter a word: ")
b=len(a)
if b%2==0:
    print("Word must me of odd number of characters")
    midchar=a[int((b-2)/2):int((b+2)/2)]
    print("The middle character is",midchar)
else:
    midchar=a[int((b-1)/2)]
    print("The middle character is: ",midchar)
