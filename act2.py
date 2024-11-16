dict1={"name":"Mahika","Age":15,"grade":11}
print ("dictionary is",dict1)

dict1["state"]="Delhi"
print("the updated dictionary is",dict1)

print('the name is',dict1.get("name") )
dict1.pop('Age')
print("the dictionary is",dict1)