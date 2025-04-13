# super key work access the parent constuctor


class a():

    def __init__(self):  # this is constructor
        print("A")

    def display(self):
        print("yes you are in class a")

class b(a):
    def __init__(self):
        super().__init__()     # access the parent class constutor and function
        # super().display()
        print("B")

    def display(self):
        print("no you are in class b")

class c(b,a):   # kind of acces argumnet must be reverse when middle of class refered to some class function as a parent
    def __init__(self):
        super().__init__()   
        print("C")

 

# obj1 = b()

obj1 = c()
