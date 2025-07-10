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


product_brand= "Hyundai creta"
product_rating= 4.6
product_price=11,60,000
seating_capacity=5
Fuel_tank_capacity="50litres"
no_of_cylinders=4
Ground_clearance_unladen="190mm"
transmission_type="automatic"
body_type="suv"
engine_displacement="1493cc"
mileage="19.1kmpl"
max_power="114bhp@4000rpm"
Fuel_type="Diesel"
max_torque="250Nm@1500-2750rpm"
air_bag_present=True 

print(product_brand)
print(product_rating)
print(seating_capacity)
print(Fuel_tank_capacity)
print(no_of_cylinders)
print(transmission_type)
print(body_type)
print(engine_displacement)
print(mileage)
print(max_power)
print(Fuel_type)
print(max_torque)
print(air_bag_present)