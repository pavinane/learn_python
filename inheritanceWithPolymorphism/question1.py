# question 1 : In area using to create shape method of calculation  and return the area of rectange


# class shape():
#    def area(self):
#     return 0


# class rectangle(shape):
#   def area(self,a=0,b=0):
#     print(a*b) 

# shape()

# r= rectangle()
# r.area(10,2)

# question 2

# class person():
#   def __init__(self,name):
#     self.name = name


# class student(person):
#   def __init__(self,name,grade):
#     super().__init__(name)
#     self.grade = grade
#   def display(self):
#     print(f"{self.name} is {self.grade} grade")

# s = student("Pavi","A")
# s.display()


# question 3

# class vehicle():
#     def start(self):
#         print("Vehicle Started")

# class car(vehicle):
#     def start(self):
#         print("Car started")

# v= car()
# v.start()

# question 4

class employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class manager(employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department
    
    def designation(self):
        print(self.name ,"salry is",self.salary,self.department)

obj = manager("pavi","50k","software Engineer")
obj.designation()    
