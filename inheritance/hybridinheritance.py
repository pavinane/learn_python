# when a  function  have single, multiple, multilevel, hierarical inheritance is called hybrid inheritance

# when two function access another function passed on argument  and remaining function only one function 
# pass argument is called on hybrid inheritance 


class dad():
    def money(self):
        print("dad's money")

class land():
    def lands():
        print("Lands to buy")


class son1(dad,land):
    pass

class son2(dad):
    pass

class son3(dad):
    pass

s1 = son1()
s2 = son2()
s3 = son3()

s1.money()