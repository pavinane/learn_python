#  inheritance have different types

# single inheritance
# multiple inheritance
# multilevel inheritance
# hierarical inheritance
# hybrid inheritance


class dad():
    def mobile(self):
        print("Dad have mobile")


# connection the two class function access the some method on one class function and that method using on
#  another function is called single inheritance


# This kind of below function pass an arugument fuction on multiple function is called multilevel inheritance

class mom(dad):       # one function pass on argument is called single inheritance     
    def sweet(self):
        print("Mom have sweet")

class son(mom):      # multile function pass on argument is called multiple inheritance    
    def laptop(self):
        print("Son have laptop")

pavi = son()
pavi.laptop()
pavi.mobile()
pavi.sweet()