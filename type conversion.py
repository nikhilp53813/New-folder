#type conversion
a=100 #int
b=3.5 #float
c=a+b #python will convert it to float automatically
print(c)
print(type(c))

#Type casting - no data loss
x = 100
y = float(x) # y should be float
print(x)
print(y)
print(type(y))

#Type casting - data loss
l = 3.14
m = int(l)#l should be int
print(l)
print(m)
print(type(m))

#text to numeric or vice versa
x="100"
y=int(x)+10
#y=x+10--> Type error: can only concacetate str (not "int") to str

print(y)
print(type(y))

z = 10 # int
num_text = str(z)
print(type(num_text))


