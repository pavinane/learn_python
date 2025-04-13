file = open("fruits.txt","a")
file.write("blueberry\n")
file.write("grapes\n")

file.close()

file = open("fruits.txt","r+")
print(
file.read()
)



