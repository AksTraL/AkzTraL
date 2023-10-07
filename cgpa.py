x= int(input("Enter your marks in DE&LA"))
u= int(input("Enter your marks in English & Comms."))
a= int(input("Enter your marks in BEE"))
b= int(input("Enter your marks in B.Etc"))
c= int(input("Enter your marks in Chemistry"))
s= int(input("Enter your marks in Electives"))
m=x+u+a+b+c+s
p= m*100/240
cgpa= p/10
print("your total marks is", m)
print("your percentage is",p,"%")
print("your cgpa is",cgpa)

if(cgpa>9):
  print("Your grade is O")

if(8<cgpa<=9):
  print("Your grade is E")

if(7<cgpa<=8):
  print("Your grade is A")

if(6<cgpa<=7):
  print("Your grade is B")

if(5<cgpa<=6):
  print("Your grade is C")

if(4<cgpa<=5):
  print("Your grade is D")

if(3<cgpa<=4):
  print("Your grade is F")
  
