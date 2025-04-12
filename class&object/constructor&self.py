
# Constructor and self keyword

# Constructor : It is a unique function thats get called automatically when a object created of a class 

# class laptop():

#     def __init__(self):   # when class the class init funtion loading on initialy 
#         self.ram="",
#         self.processor=""
    
#     def display(self):
#         print("ram",self.ram)
#         print("processor",self.processor)


# hp = laptop()
# dell = laptop()

# hp.ram = "8bg"
# dell.ram = "4gb"

# hp.processor = "i5"
# dell.processor = "i8"

# hp.display()
# dell.display()


# example 1

# class student():
#     name ="",
#     register_num = 0
    
    # def display(self):
    #     print(f"name : {self.name} , register : {self.register_num}")


# hallticket = student()
# hallticket.name = "pavi"
# hallticket.register_num = 5111715114945

# hallticket.display()


# Example 2

# class fruit:
    # def __init__(self,color):
    #     self.color =color
        
# apple = fruit("red")

# print(apple.color)


# Example 3

# class Teacher:
    
#     def __init__(self,name,register):
#         self.name =name
#         self.register =register

#     def display(self):
#         print(f"name : {self.name} , register : {self.register}")


# t1 = Teacher("vaishu",9995059)
# t2 = Teacher("keerthi",7540016)

# t1.display()
# t2.display()


# Example 4

class Calculator:
    
    def __init__(self,a,b):
        self.a =a
        self.b =b

    def add(self):
        print(f"addition : {self.a + self.b} ")
    
    def sub(self):
        print(f"substraction : {self.a - self.b} ")

    def mul(self):
        print(f"multiplication : {self.a * self.b} ")
    
    def div(self):
        print(f"division : {self.a / self.b} ")




t1 = Calculator(10,2)
t2 = Calculator(5,10)
t3 = Calculator(2,10)
t4 = Calculator(10,2)

t1.add()
t2.sub()
t3.mul()
t4.div()








