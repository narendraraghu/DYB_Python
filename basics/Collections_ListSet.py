# in java List<String> list = new ArrayList<>();
# create a new list
list_of_bla_bla = ["A", "E", "C"]
list_of_bla_bla.insert(3, "D")  # insert at an index
sorted_list = sorted(list_of_bla_bla)  # returns a new, sorted list
print(list_of_bla_bla)
list_of_bla_bla.sort()  # in place sort
print(list_of_bla_bla)
list_of_bla_bla.remove("C")  # remov        e first occurrence of "C"
popped = list_of_bla_bla.pop(2)  # return and remove the item at index 2
list_of_bla_bla.reverse()  # reverse the list
a = list_of_bla_bla.index("A")  # return index of "A"
list_of_bla_bla += ["E", "F"]  # add a list with E and F to the end of this list
size = len(list_of_bla_bla)  # size of the list

# Sets

# In java Set<String> set1 = new HashSet<>();

set_of_words1 = set()  # create a new set. Note that we do not use {}, as that is for the dict
set_of_words1.add("The")  # add values
set_of_words1.add("A")
set_of_words1.add("Boat")
print("Boat" in set_of_words1)  # True
set_of_words2 = {"Anchor", "A", "Coast"}  # create another set and populate it
print(set_of_words1.intersection(set_of_words2))  # intersection  {'A'}
print(set_of_words1.union(set_of_words2))  # union  {'Coast', 'Anchor', 'Boat', 'A', 'The'}
for value in set_of_words2:  # all values
    print(value)
