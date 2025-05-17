dic = {"John":82 , "Micheal":99 , "Adam":22 , "Abhinav":100}
name = str(input("Enter the student's name: "))

marks = dic.get(name , "Student not found!")

if name in dic:
  print(name,"'s marks : ",marks)
  
else:
    print(marks)

