from functools import reduce

add=lambda a,b:a+b
result=add(3,5)
print(result)

num=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda n:n%2==0,num))
print(even)

double=list(map(lambda n:n*2,even))
print(double)

sum=reduce(lambda a,b:a+b,double)
print(sum)+
