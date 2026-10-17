#Q) Create a function to check max number between two number :
def max(a,b):
    if a>b:
        print(a,"is max")
    else:
        print(b,"is max")
a=int(input("Enter first number :"))
b=int(input("Enter a second number :"))
max(a,b)