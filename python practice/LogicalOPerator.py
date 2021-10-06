x=int(input("Enter num :"))
y=int(input("Enter num :"))
z=int(input("Enter num :"))
if x>y and x>z:
    print(x)
elif y>x and y>z:
    print(y)
else :
    print(z)       

ch=str(input("Enter letter :"))
if ch=='a'or ch=='e'or ch=='i'or ch=='o'or ch=='u':
    print("VOWEL")
else:
    print("CONSONANT")    