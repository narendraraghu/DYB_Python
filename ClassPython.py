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
clz = MyClass(["foo", "bar"])
print(clz.count())  # will print 2
print(clz.words)  # will print ['foo','bar']


# Example file for working with classes
class myClass():
    def method1(self):
        print("Guru99")

    def method2(self, someString):
        print("Software Testing:" + someString)


def main():
    # exercise the class methods
    c = myClass()
    c.method1()
    c.method2(" Testing is fun")


if __name__ == "__main__":
    main()

# Python  Constructors  Itbegins with a double underscore (_).It __init__() method

class User:
    name = ""

    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print("Welcome to Python constructor, " + self.name)

User1 = User("Narendra Raghuwanshi")
User1.sayHello()