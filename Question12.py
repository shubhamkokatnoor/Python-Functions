#Q) WAP to check a given number is even or odd :
def evenodd():
    n=int(input("Enter a number :"))
    if n%2==0:
        return True
    else:
        return False
res=evenodd()
if res==True:
        print("Number is even")
else:
        print("Number is odd")