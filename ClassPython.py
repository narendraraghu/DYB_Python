class MyClass:
    words = []

    def __init__(self, data=["Narendra"]):  # think of this as a Constructor in Java
        self.words = data

    def count(self):  # think of self as "this" in Java
        return len(self.words)

# Usage
clz = MyClass()
print(clz.count())  # will print 1
print(clz.words)  # will print ['Narendra']
clz = MyClass(["foo","bar"])
print(clz.count())  # will print 2
print(clz.words)  # will print ['foo','bar']

