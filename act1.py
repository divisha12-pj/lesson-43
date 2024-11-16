fruits=["litchi","mango","pineapple","strwaberry"]
print("the org ;ist is",fruits)

print(fruits[3])
print(fruits[1:4])
print(len(fruits))

fruits.append("guava")
print("the updated list 1 is",fruits)
fruits.remove("litchi")
print("the updated list 2 is",fruits)

fruits.pop(2)
print("the updated list 3 is",fruits)
fruits.clear()
print("the updated list is",fruits)