class Emp:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal

    def disp(self):
        print('eid:',self.eid)
        print('ename:',self.ename)
        print('sal:',self.sal)

e1=Emp(23,'ravi',20000)
e1.disp()