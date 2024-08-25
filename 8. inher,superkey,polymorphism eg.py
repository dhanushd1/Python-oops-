class shape:
    def area(self):
        return 0
class rectangle(shape):
    def area(self):
        l=10
        b=20
        print(l*b)
        
    
        
ob1=rectangle()
ob1.area()

#___________________________________________________________

class person:
    def __init__(self,name):
        self.name=name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
        
    def display(self):
        print(self.name,self.grade)



s1=student("john","A")
s1.display()

#____________________________________________________________

class vehicle:
    def start(self):
        print("vehicle started")
class car(vehicle):
    def start(self):
        print("car started")

v1=car()
v1.start()
    
#_______________________________________________________________

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
class manager(employee):
    
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department

    def method(self):
        print(self.name,self.salary,self.department)

m=manager("raj",2000,"it")
m.method()       



