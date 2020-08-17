pos=-1
def search(list,n):

    for i in list:
        if i==n:
            return i
list=[3,5,7,9,4]
n=int(input('enter number'))
if search(list,n):
    print('element found')
else:
    print('element not found')
