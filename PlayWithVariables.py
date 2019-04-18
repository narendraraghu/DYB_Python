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
bool(value)  # Will only return false for an empty string or an int=0

print(bool(value))

list_of_strings = {'1', '2', '3'}
list_of_ints = [int(i) for i in list_of_strings]
print(list_of_ints)

a = 100
print(a)

a = "Narendra"
b = 99
# print(a+b)

# TypeError: can only concatenate str (not "int") to str

a = "Narendra"
b = "99"
print(a + b)

# below can concatenate both
a = "Narendra"
b = 99
print(a + str(b))
# In Python you cannot concatenate string with number directly,
# you need to declare them as a separate variable, and after that, you can concatenate number with string

var = "deleteME"
print(var)

del var
# print(var) you will get error here because the variable is deleted


x = "Narendra"
y = "99"
print(x * 2)
# star is used for  (*)	Repeat

x = "Narendra"
print(x[1])  # Slice- it gives the letter from the given index
# In slicing, if range is declared [1:5], it can actually fetch the value from range [1:4]


name = 'Narendra'
number = 99
print('%s %d' % (name, number))

one = "narendra"
two = one.capitalize()
three = one.replace('narendra', 'R')
print(two)
print(three)

string = "python"  # PYTHON
print(string.upper())

print(":".join("Narendra"))  # N:a:r:e:n:d:r:a
print(''.join(reversed(one)))

print(one.split('r'))  # ['na', 'end', 'a']
msg = "In the same case if you want to split me"

print(msg.split(' '))  # ['In', 'the', 'same', 'case', 'if', 'you', 'want', 'to', 'split', 'me']

# In Python, Strings are immutable. same way like java

x = "Narendra"
x.replace("Narendra", "Raghuwanshi")
print(x)

# you have to assign like below
x = "Narendra"
x = x.replace("Narendra", "Raghuwanshi")
print(x)
