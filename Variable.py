#examples of immutable data (numbers,decimals,simple text)
value_num=10
value_rating=5
value_name="Satish"

print (id(value_num))
print (id(value_rating))
print  (id(value_name))

value_newrating=4.8
print (id(value_num))
print (id(value_rating))
print  (id(value_name))

print (id(value_newrating))

#example of mutable data
list1 = (1,2,3)
list2 = (4,5,6)
list3 = (8,9,10)

print (id(list1))
print (id(list2))
print (id(list3))

# type function defines what data types is being assigned for variable

print(type(value_name))
print(type(value_rating))
print(type(value_num))

#output variable
msg= "python is awesome"
print(msg)

x="python"
y="is"
z="awesome" 

print(x+y+z)
version = 3
version_old = 2

print(x+y+z)
print(version+version_old)

#print python is awesome 3
print(msg,version) 

#many values to multiple variables
#no of variables must be equal to no of values
x,y,z = "python","is","awesome"
print(x,y,z)

#one values to multiple variables

x = y = z = "python"
print(x,y,z)

#ProductName -->Pascal case(class Names)
#productName-->Camel case(objectNames)
#product_name-->Snake case (When using variables and functions)


