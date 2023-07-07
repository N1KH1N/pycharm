# oop variale type
# instance variable  --  related to methods  --  self
# static variable  --  related to class  --  class name

class Student:
    col="sngc"
    def setvalue(self,name,rollno,dep):
        self.name=name
        self.no=rollno
        self.dep=dep
    def printv(self):
        print(self.name)
        print(self.no,self.dep)
        print(Student.col)
s1=Student()
s1.setvalue("nikhin",21,"bca")
s1.printv()

s2=Student()
s2.setvalue("anurag",22,"bsccs")
s2.printv()