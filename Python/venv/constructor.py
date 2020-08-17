#using loal variables in different methods
# can be achieved by converting local variables into class variables
class Con:
    #def add(self,a,b):
    def __init__(self,a,b):
        print(a+b)
        self.a=a # converting local variables to class variables
        self.b=b
    def sub(self):
        print(self.a-self.b) #using class variables

co=Con(30,20)
#co.add(30,20)
co.sub()