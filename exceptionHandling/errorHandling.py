# exception hamdling is called error handling


# complile Error : while compile the variable or function or other while compiling show the error is called compailing error

# print("Hellow word")

# printt("bye")


# Logical Error : it not showing any other error msg but logicaly is wrongly printed 

# a=10
# b=5
# print(a+a)



# Runtime Error : It will show error because assign value of worng datatypes that is called runtime error
# a = int(input("Enter number of a"))
# b= int(input("Enter number of b"))

# print(a+b)

# exceptional error handling : It can handling the error 

# try:
#     a = int(input("Enter number of a"))
#     b= int(input("Enter number of b"))
#     print(a+b)

# except Exception as e:
#     print("Something went wrong",e)

# Example 2
try:
    a = input("Enter value of a ")
    b= input("Enter value of b ")
    print(a/b)
    print(d)

# except Exception as e:   # all type of error will show
#     print("Something went wrong",e)

except ValueError as e:   # only value error show
    print("value error went wrong",e)

except TypeError as e:   # only type error show
    print("type error went wrong",e)

finally:
    print("done")