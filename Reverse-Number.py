#Reverse Number 
a=int(input("Enter the Number:"))
rev=0

while a>0:

    rem=a%10
    rev=rev*10+rem
    a=a//10

if a==rev:
    print("The Number Is Reverse:",rev)
else:
    print("The Number Is Not Reverse:",rev)
