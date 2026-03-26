print ("Hello World")

# Identation
if 5 > 2:
    print ("Five is greater than two!")
print()

# Multiple words on the same line
print ("Two is greater than one!", end="")
print (" Five is also greater than one!")
print()

# Printing Numbers
print (5, 3 + 2)
print ("I am", 24, "years old!")
print ()

# Data TYpes
a = "Hello World"
b = 20	
c = 20.5
d = 1j
e = ["apple", "banana", "cherry"]
f = ("apple", "banana", "cherry")	
g = range(6)
h = {"name" : "John", "age" : 36}	
i = {"apple", "banana", "cherry"}
j = frozenset({"apple", "banana", "cherry"})
k = True
l = b"Hello"
m = bytearray(5)
n = memoryview(bytes(5))
o = None
print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h), type(i), type(j), type(k), type(l), type(m), type(n), type(o))
print()

# Conversion
x = 3
y = 2.8
z = 1j

a = float (x)
b = int (y)
c = complex (z)

print (a, b, c)
print()

print(type(a), type(b), type(c))
