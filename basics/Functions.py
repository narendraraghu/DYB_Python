def add(x, y):
    return x + y  # If return is skipped, the method returns a None


print(add(1, 2))

# Can be called with named arguments

# print(add(x=5,y=7)) # Will print 12
print(add(y=51, x=7))  # Will print 12


# Can take default arguments too
def add(x, y=2):
    return x + y


print(add(5))  # Will return 7


# Function defined by the def statement
# The code block within every function starts with a colon (:) and should be indented (space)
def test():
    print("Narendra")
    print("Raghuwanshi")


test()
