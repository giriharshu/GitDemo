def sum(*args):
    s=0
    for i in args:
        s+=i
    return s


s=sum(1,5,8,9)
print(s)