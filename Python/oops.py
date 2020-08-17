a,b=10, #global variable
class Myclass:
    a,b=30,40 #class variable
    def add(self,a,b): #local variable
        print(a+b)
        print(self.a+self.b)
        print(globals()['a']+globals()['b'])

m1=Myclass()
m1.add(100,200)