# Dictionary : Do not allow duplicate , duplicate value will be overwrite the existing value
# Allow any type of datatype
# It have key and value pair

# a= {"name":"Pavi"}

# print(a)
# print(a["name"])

b ={
    "name":"nane",
    "age":28,
    "location":"chennai",
    "friends" : ["soma","boobalan","mukesh","vicky"]
}

# print(b.keys())
# print(b.values())

# Modify
# b["name"] = "pavimegan" 
# or
# b.update({"name":"nane"})
# print(b)

# Add
# b["color"] = "green"
# print (b)

# Delete
# b.pop("age")
# or 
# del b["location"]  # if complete delete the data jsst (del b) is enough delete entire data
# print(b)

# Clear  : clear all values inside the object
b.clear()
print(b)