a=[1,45,78,88,99,100]
n=99
l=0
u=len(a)-1
for i in range(u):
    if l<=u:
        mid=(l+u)//2
        if a[mid]==n:
            break
        else:
            if a[mid]<n:
                l=mid+1
            else:
                u=mid-1
                break
print(a[mid])

