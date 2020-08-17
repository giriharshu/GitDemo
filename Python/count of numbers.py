
def countnum(n):
    count=0
    while n>0:
        count=count+1
        n=n//10
    return count
n=int(input('enter number'))
print(countnum(n))
