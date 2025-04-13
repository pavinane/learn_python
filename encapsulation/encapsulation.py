# Encapsulation : it can't be override , only use the variable to update use another function , that is called encapsulation

# company = public variable : update the value easy
# _company = protected variable :update the value on normal way and it used through inheritance secenario also
# __company = private variable : update the value not possibele initaly but it can override the value by using another function


# private variable

# class company():
#     # when insert __ before the variable is called private variable it cannot be override unless use to declare another function
#     def __init__(self):
#         self.__company ="Facebook"   

#     def companyName(self):
#         self.__company = "fb"   # this is way to private variable to override to change the value
#         print(self.__company)


# c1 = company()
# c1.companyName()


#protected variable

class company():
    # when insert __ before the variable is called private variable it cannot be override unless use to declare another function
    def __init__(self):
        self._company ="fb"   



class shellcompany(company):
    pass



b = shellcompany()
print(b._company)
