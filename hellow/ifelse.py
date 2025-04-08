# Example 1

# rcb = "win"
# if (rcb == "win"):
#     print("Rcb won the match")
# else :
#     print ("Rub lose the match")


# Example 2

# user  = input()
# if(user == "pavi"):
#     print("If condition working pavi")
# else:
#     print("else condition working pavi")

# Example 3

# user  = input("Enter name ")
# if(user == "pavi"):
#     print("If condition working pavi")
# else:
#     print("else condition working pavi")


# Example 4

# score = int(input("Enter Mark"))

# if(score >35):
#     print("Pass the exam")
# else:
#     print ("Fail the exam")
    
# Example 5 

# a = int(input("Enter number: "))
# if(a%3 == 0 and a%5 == 0):
#     print("divisible by both 3 and 5")
# elif (a%3 == 0 ):
#     print("divisible by 3 only")
# elif (a%5 ==0):
#     print("Divisible by 5 only")
# else :
#     print("Not divisible by 3 and 5")


#Example 6

# score = int(input("Enter Score: "))
# if(score <35):
#     print("Poor Student")
# elif (score >35 and score <70 ):
#     print("Average Student")
# elif (score >70 and score< 100):
#     print("Good Student")
# else :
#     print("Input is invalid")


# Example 7

# value = int(input("Enter value: "))
# if(value%2 == 0):
#     print ("Value is even")
# else: 
#     print("value is odd")


# Example 7

# value1 = int(input("Enter value: "))
# value2 = int(input("Enter value: "))
# method = input("Enter Method : ")

# if(method=="add"):
#     print(f"Method addition result is ${value1 + value2}")
# elif(method=="sub"):
#     print(f"Method substraction result is ${value1 - value2}")
# elif(method=="mul"):
#     print(f"Method multiplication result is ${value1 * value2}")
# elif(method=="div"):
#     print(f"Method division result is ${value1 / value2}")
# else:
#     print("Method are invalid")


# Example 8

# percentage = int(input("Enter percentage: "))


# if(percentage >= 70):
#     name = input("Enter name: ")
#     department = input("Enter department : ")
#     location = input("Enter location : ")
   
#     print("You are eligible")
# else :
#     print("You are not eligible")



# Example 9

salary = int(input("Enter salary : "))
age = int(input("Enter age : "))

if(salary >= 20000 or age <= 25):
    loan = int(input("Enter loan amount: "))
    if(loan <= 50000):
        print("Loan amount eligible")
    else:
        print("Your are not eligible for loan")
else:
    print ("Your are not eligible for loan")


