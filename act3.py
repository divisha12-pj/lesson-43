def listtodict(lst):
  mydict={}
  for item in lst:
     mydict[item[0]]=item[1:]

 
  return mydict
 

student=[[1,"genelia",3],[2,"bhav",2],[3,"dhwani",4]]
print("list is ",student)
print("the converted list is",listtodict(student))