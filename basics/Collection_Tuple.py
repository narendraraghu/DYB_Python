# There are no Tuples in Java. A tuple is an immutable collection of values
# Tuples are hashable, and list are not


words = ("Good", "Morning")  # or words = "Good", "Morning"
print("Good" in words)  # True
print("narendra" in words)  # False
print(hash(words))  # This is what makes the tuples so special - they are hashable
a, b = words  # or a,b = "Good", "Morning"
print(a)  # Good
print(b)  # Morning
print(len(words))  # 2

x = ("TFS", 20, "Developer")  # tuple packing
(company, emp, profile) = x  # tuple unpacking
print(company)
print(emp)
print(profile)

# The comparison starts with a first element of each tuple.
# If they do not compare to =,< or > then it proceed to the second element and so on.
a = (1, 1)
b = (1, 4)
if a > b:
    print("a is bigger")
else:
    print("b is bigger")

a = {'x': 100, 'y': 200}
b = list(a.items())
print(b)

# Slicing of Tuple
# To fetch specific sets of sub-elements from tuple or list, we use this unique function called slicing.
# Slicing is not only applicable to tuple but also for array and list.
x = ("a", "b", "c", "d", "e")
print(x[2:4])

# Slicing always start with 0 and stop exact before the end point.


Dict = {'Tim': 18, 'Charlie': 12, "Joe": 22, 'Robert': 25}
print(Dict['Joe'])

# Create initialized dictionary
d1 = {5: "number", "to": "string"}
print("Dictionary contents")
print("Key", ' : ', "Value")
for x in d1.keys():
    print(x, ' : ', d1[x])

d2 = {1: 12, 2: 13, 3: 14}
print(d2[1])

# Updating
Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
Dict.update({"Sarah": 9})
Dict.update({"Tim": 91})
print(Dict)

del Dict['Charlie']
print(Dict)

print("Students Name: %s" % list(Dict.items()))

#  Check if a given key already exists in a dictionary
Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
Boys = {'Tim': 18, 'Charlie': 12, 'Robert': 25}
Girls = {'Tiffany': 22}
for key in list(Dict.keys()):
    if key in list(Boys.keys()):
        print(True)
    else:
        print(False)

# Sorting the Dictionary
Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
Boys = {'Tim': 18, 'Charlie': 12, 'Robert': 25}
Girls = {'Tiffany': 22}
Students = list(Dict.keys())
Students.sort()
for S in Students:
    print(":".join((S, str(Dict[S]))))

print("Length : %d" % len(Dict))
print("variable Type: %s" % type(Dict))
print("printable string:%s" % str(Dict))
print(Dict)

# Method	Description	                                                                Syntax
# copy()	Copy the entire dictionary to new dictionary	                            dict.copy()
# update()	Update a dictionary by adding a new entry or a key-value pair to an
# existing  entry or by deleting an existing entry.	                                    Dict.update([other])
# items()	Returns a list of tuple pairs (Keys, Value) in the dictionary.	            dictionary.items()
# sort()	You can sort the elements	                                                dictionary.sort()
# len()	    Gives the number of pairs in the dictionary.	                            len(dict)
# cmp()	    Compare values and keys of two dictionaries	                                cmp(dict1, dict2)
# Str() 	Make a dictionary into a printable string format	                        Str(dict)
