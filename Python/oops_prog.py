class Student:
    school_name='IPS'
    area='RT Nagar'
    km=10

    def __init__(self,name,age,clas):
        self.name=name
        self.age=age
        self.clas=clas

    def disp_school(self):
        print('school details:',self.school_name,self.area,self.km)

    def disp_student(self):
        print('student details:',self.name,self.age,self.clas)

    @classmethod
    def update_school(cls):
        n=int(input('press 1 school_name \n2 for area \n3 km'))
        if n==1:
            cls.school_name=input('enter school name')
        elif n==2:
            cls.area=input('enter the area')
        elif n==3:
            cls.km=input('enter km')
        else:
            cls.school_name=input('enter school name')
            cls.area = input('enter the area')
            cls.km = input('enter km')

    def update_student(self):
        n=int(input('press 1 name \n2 age \n3 class'))
        if n==1:
            self.name=input('enter student name')
        elif n==2:
            self.age=input('enter student age')
        elif n==3:
            self.clas=input('enter student clas')
        else:
            self.name = input('enter student name')
            self.age = input('enter student age')
            self.clas = input('enter student clas')



stu1=Student('ravi',23,'10th')
stu1.disp_school()
stu1.disp_student()
stu1.update_school()
stu1.update_student()
stu1.disp_school()
stu1.disp_student()