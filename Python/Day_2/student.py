class Student:
    def __init__(self,student_id,student_name):
        self.student_id=student_id
        self.student_name=student_name
    def display(self):
        return self.student_id,self.student_name
std1=Student(22790,'sai')

display1=std1.display()
print(display1)
setattr(std1,'student_class',10)
print(getattr(std1,'student_class'))
print(hasattr(std1,"student_class"))
delattr(std1,"student_class")
print(hasattr(std1,"student_class"))
std1=Student(22790,"sai kiran")
display1=std1.display()
print((display1))
setattr(std1,'__studentdept',5)
print(getattr(std1,'__studentdept'))