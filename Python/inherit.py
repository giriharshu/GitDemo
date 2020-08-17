c=30
d=40
class A:
    a=10
    b=20
    def dis(self):
        print("car")
class B(A):
    e=50
    f=60
    def disp(self,t,h):
        print(t+h)
        print(self.e+self.f)
        print(self.a+self.b)
        print("bike")
        #super().disp()
ob=B()
ob.disp(70,80)
