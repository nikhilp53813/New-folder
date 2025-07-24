#simple condition check
#5>2-->true
#2>5-->false

if 5>2:
 print("5 is greater than 2")

 #if statments checks if the condition is true or false
 num=5
 if num>5:
  print("positive number")
num1=-2
if num1>2:
 print("positive number")

 # tell me condition to check if the given number is in range
# 10 - 20
num=12
if num >=10 and num<=20 :
 print(f"the given number{num}is in range")

 # if-else statement
# if condition:
#     statements
# else:
#     statements
num=10
if num>=0:
 print("positive number")
else:
 print("negative number")
 
 
#vote app
 age = 24
 if age>=18:
  print("you can vote")
 else:
  print("you cannot vote")

#input function demo
name= input("Enter yout name:")
print(f"welcome{name}")
age=input("Enter your age")
print(f"welcome:{name}your age is {age}")
 

 #VOTER APP Dynamic
age=int(input("Enter your age"))
age = 24
if age>=18:
     print("you can vote")
else:
    print("you cannot vote")

#ternary operators
#value_if_true if conditions else value_if_false
age=int(input("Enter your age"))
vote_status="you can vote"if age>=18 else"you cannot vote"
print(vote_status)

# elif ladder
# if condition:
#     statements
# elif condition:
#     statements
# elif condition:
#     statements
# elif condition:
#     statements
# else:
#     statements

#example of systems below
marks=int(input("enter your marks:"))
if marks>=90:
  print("A")
elif marks>=80:
 print("B")
elif marks>=70:
 print ( "c")
elif marks>=60:
  print  ("D")
else :
  print("FAIL")

# vote app with id card
has_id=True
age=int(input("Enter your age"))
if age>=18:
 if has_id:
   print("you are allowed to voting center")
 else:
  print(" you can not vote")

# vote app with nationality
age=int(input("Enter your age"))
nationality=(input("enter your nationality"))
if age>=18 and nationality=="Indian":
  print("you are allowed to vote")
else:
  print("you cannot vote")



