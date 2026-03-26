# Quote inside Quote
print ("It's fine")
print ("They also call me 'Ajuski'")

# Multiline Strings
a = """
I must not fear,
Fear is the mind-killer.
Fear is the little-death that brings total obliteration.
I will face my fear.
I will permit it to pass over me and through me.
And when it has gone past I will turn the inner eye to see its path.
Where the fear has gone there will be nothing.
Only I will remain.
"""
print (a)

# Strings are Arrays
a = "Hello World"
print (a[0] + "\n")

# Slicing
print (a[0:4])
print (a[-5:])
print (a[7] + a[9] + a[10] + "\n")

# Check String
msg = "Hello World"
print(len(msg))
if "Hello" in msg:
    print ("Yes, spelling is correct.")  
else:    print ("No, spelling is incorrect.")

if "World" not in msg:
    print ("No, message is incomplete.")
else:    print ("Yes, message is complete." + "\n" )   

# Modify String
a = "Hello World"
print (a.upper())
print (a.lower())
print (a.replace("H", "J"))
print (a.split(" "))
print (a.strip("H"))
print ()

# Concatination
a = "Hello"
b = "World"
c = a + " " + b
print (c + "\n")


# Formatting
age = 24
txt = f"I am {age} years old."
print (txt + "\n")

# Methods
a = "Hello World"
print (a.capitalize())
print (a.casefold()) 
print (a.center(20, "x"))
print (a.count("l"))
print (a.encode())
print (a.endswith("d"))
print (a.expandtabs())
print (a.find("o"))
print (a.format())
print (a.index("o"))
print (a.isalnum())
print (a.isalpha())
print (a.isdecimal())
print (a.isdigit())
print (a.isidentifier())
print (a.islower())
print (a.isnumeric())
print (a.isprintable())
print (a.isspace())
print (a.istitle())
print (a.isupper())
print (a.join("123"))
print (a.ljust(20, "x"))
print (a.lower())
print (a.lstrip("H"))
print (a.maketrans("H", "J"))
print (a.partition("o"))
