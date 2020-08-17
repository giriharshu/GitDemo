#How to call current class method in another method
class Myclass:
    def add(self,a,b):
        print(a+b)
        self.sub(50,40)
    def sub(self,c,d):
        print(c-d)

oc=Myclass()
oc.add(30,50)