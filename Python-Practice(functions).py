 def sum(a,b):
    sum=a+b
    print(sum)
    return sum  # or return a+b


sum(3,4)

sum(7,8)

sum(1,3)


#recursion

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    print("End")


show(5)




