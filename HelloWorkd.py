def main():
    print("hello world!")
print("hello again")

# This is a comment

# It is because we did not declare the call function "if__name__== "__main__".


# When Python interpreter reads a source file, it will execute all the code found in it.
# When Python runs the "source file" as the main program, it sets the special variable (__name__) to have a value ("__main__").
# When you execute the main function, it will then read the "if" statement and checks whether __name__ does equal to __main__.
# In Python "if__name__== "__main__" allows you to run the Python files either as reusable modules or standalone programs.



if __name__ == "__main__":
    main()

    # With newline
    print("Hello World");
    # Without newline
    print("Hello World", end='')
