# Dictionaries

fruits = {
    "apple" : "green", 
    "banana" : "yellow", 
    "cherry" : "red"
}

print("Actual Dictionaries -->",fruits)

print("Accessing Dictionaries -->",fruits["apple"])

fruits["apple"] = "orange"

print("New value of apple furits -->",fruits)

fruits["jackfruit"] = "light Green"

print("Added new key value pair in fruits -->", fruits)

del fruits["banana"]

print("Deleted a key banana --> " , fruits)
