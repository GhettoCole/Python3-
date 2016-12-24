# Assertions - A sanity-check that you can turn on or off when you have finished testing  program
# An expression is tested, and if the result comes up false, an exception is raised
# Assertions are carried out through use of the assert statement

try:
    print(1)
    assert 2 + 2 == 4
    print(2)
    assert 1 + 1 == 3
    print(3)
    """
    Programmers often place assertions at the start of a function to check for valid input
    and after a function call to check for a valid output
    """

    print(0)
    assert "h" != "w"
    print(1)
    assert False
    print(2)
    assert True
    print(3)

    # The assert can take a second argument that is passed to the AssertionError raised if the assertion fails
    temp = -10
    assert(temp >= 0), "Colder than absolute zero!"
    
    """
    AssertionError exceptions can be caught and handled like any other exception
    using the try/except statement, if not handled this type of exception will
    terminate the program
    """
except AssertionError:
    print("Errors occured")
finally:
    def my_func(x):
        assert x > 0, "Error"
        print(x)
