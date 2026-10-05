#Q) Find given number factorial :
def fact():
    f = 1
    n = int(input("enter a number :"))

    for i in range(n,0,-1):
        f = f*i
    print("factoria is",f)
fact()