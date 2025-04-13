# The word of polymorphism means having many other forms . In programing polymorphism means the same function name
# (but different signature) being used for different types. The key difference is that types and number of arguments used in function

# def add (a,b,c=0):
#     print(a+b +c)

# add(5,2)
# add(5,2,3)


# Example 1

class animals():
    def sound(self):
        print("Animal make sound")

class dog(animals):
      def sound(self):
        print("dog barks")

class bird(animals):
    def sound(self):
        print("Birds sing")

a1 = dog()
a1.sound()

b1 = bird()
b1.sound()