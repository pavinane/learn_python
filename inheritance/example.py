# This is hierarical inheritance

# a single function access multiple fulction is called  hierarical inheritance

class dad():
    def money(self):
        print("dad's money")


class son1(dad):
    pass

class son2(dad):
    pass

class son3(dad):
    pass

s1 = son1()
s2 = son2()
s3 = son3()

s1.money()