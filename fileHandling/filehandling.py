# file = open("frudoc.TXT")
# print(file)   # jst file showing their path but unable read

# print(file.read()) # it read the file show the content of the file
# content = file.read()
# print(content)


# read and write

# w = wrire
# r= read
# r+ = both read and write
# a = append => data added with exist data

#file.readine() => show 1st line of the data

file = open("frudoc.TXT","w")    # write acces the file but it can override already exist will erase

file.write("jackfriut")

content = file.read()
print(content)


