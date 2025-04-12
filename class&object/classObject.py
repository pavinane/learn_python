# when use class  have to defined self inside the function as argument

# example1
# class trip:
#     name ="",
#     drink = ""
#     def party(self):
#         print("Let's Party")
#     def beach( self):
#         print("Let's rock the beach")

# pavi = trip()
# nane = trip()


# # access the function inside the class
# pavi.party()  
# nane.beach()

# # access the name inside class
# pavi.name ="pavi"
# pavi.drink ="no"
# print(pavi.name , "drinker", pavi.drink)
# nane.name = "nane"
# nane.drink ="yes"
# print(nane.name, "drinker", nane.drink)


# example2 

class laptop():
    price="",
    processor="",
    ram=""

    def hp(self):
        print(f"hp laptop ")
    
    def dell(self):
        print("dell laptop")
    
    def lenevo(self):
        print("lenevo laptop")
        

lapHP=laptop()
lapHP.hp()
lapHP.price = "$100"
print("HP price",lapHP.price)

lapDELL=laptop()
lapDELL.dell()
lapDELL.price = "$100"
print("DELL price",lapDELL.price)

lapLENEVO=laptop()
lapLENEVO.lenevo()
lapLENEVO.price = "$100"
print("LENEVO price",lapLENEVO.price)