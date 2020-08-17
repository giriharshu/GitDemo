fact=1
num=int(input('enter the number'))

if num<0:
    print('not a fact')
elif num==0:
    print('0 is not a fact')
else:
    for i in range(1,num+1):
        fact=fact*i
    print('fact of',num,'is:',fact)

