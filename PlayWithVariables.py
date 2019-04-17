name = "Name"
age = 42
completed = False
c = 'A'
f = 0.0034

value = 12

# casting
int(value)
str(value)
float(value)
bool(value) # Will only return false for an empty string or an int=0

print(bool(value))

list_of_strings = {'1','2','3'}
list_of_ints = [int(i) for i in list_of_strings]
print(list_of_ints)

a=100
print(a)


a="Narendra"
b = 99
# print(a+b)

# TypeError: can only concatenate str (not "int") to str

a="Narendra"
b = "99"
print(a+b)

# below can concatenate both
a="Narendra"
b = 99
print(a+str(b))

