try:
    #   assert (1 == 1)
    assert (1 == 2)
#  assert(1==2/0)  # This will cause an error
except AssertionError:
    print("Caught Assertion Exception")
except:  # catch all exceptions
    print("Caught unknown exception")
else:  # happy path
    print("No exceptions raised")
finally:  # will execute regardless of exceptions or happy path
    print("Done with the assertion")

# Maps in JAVA : Map<String,Integer> wordCount = new HashMap<>();
# Maps are called dicts or Dictionaries in Python.

wordcount_map = {}  # create a new, empty dict
wordcount_map = {"anchor": 2, "dock": 3}  # create a new dict and add key-values

wordcount_map["the"] = 10  # add keys and values
wordcount_map["a"] = 8
wordcount_map["boat"] = "narendra"
print(wordcount_map["the"])  # value of a key
print(wordcount_map.keys())  # List of keys
print(wordcount_map.values())  # List of values
print("a" in wordcount_map)  # True
print(wordcount_map.items())  # prints tuples of key-value pairs
# print(wordcount_map["foo"]) # throws a KeyError
