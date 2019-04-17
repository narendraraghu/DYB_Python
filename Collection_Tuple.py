# There are no Tuples in Java. A tuple is an immutable collection of values


words = ("Good", "Morning")  # or words = "Good", "Morning"
print("Good" in words)  # True
print("narendra" in words)  # False
print(hash(words))  # This is what makes the tuples so special - they are hashable
a, b = words  # or a,b = "Good", "Morning"
print(a)  # Good
print(b)  # Morning
print(len(words))  # 2
