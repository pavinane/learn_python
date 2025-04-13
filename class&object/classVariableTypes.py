# class phone:
#     charger = "C-type"   # this charger variable
#     def __init__(self,mobile,price):
#         self.mobile = mobile   # self.mobile like is called instance variable
#         self.price = price
     

#     def specification(self):
#         print(f"mobiel : {self.mobile}")
#         print(f"mobiel : {self.price}")
#         print(f"mobiel : {self.charger}")

# mobile = phone("samsung","1000")

# mobile.specification()


class laptop:
    charger = "C-type"   # this charger variable
    def __init__(self,):
        self.laptop = ""   # self.mobile like is called instance variable
        self.price = 200

    def specification(self,price):
        self.price = price

    def getSpecification(self,price):
        self.price = price 
        print("price",self.price)

    @classmethod   # decreative variable
    def priceRange(cls):
        cls.charger = "B type"
        print("charger", cls.charger)
    
    @staticmethod
    def info():
        print("Static method")
       



device = laptop()

device.getSpecification(5000)

laptop.priceRange()

device.info()
