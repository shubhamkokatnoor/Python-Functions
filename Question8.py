#Q) Create function to check factorial sum :
def fact(n):
    f=1
    for i in range(n,0,-1):
        f*=i
    print("Factorial is :",f)
n=int(input("enter a number :"))
fact(n)