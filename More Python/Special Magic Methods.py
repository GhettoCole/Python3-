class Employee:
    # Creating a class variable
    apply_amount = 1.04
    number_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@Gmail.com'

        # Increment the value of employees each time an instance is created

        Employee.number_of_employees += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.apply_amount)

    # Used for escaping vague results
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # Adding pays of two instances with the use of a magic method
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


first_employee = Employee('Given', 'Lepita', 65000)
second_employee = Employee('Zad', 'Jumpy', 90000)

print(first_employee)
print("\n")
# The __repr__ magic method can still be accessed
# Other ways of calling the functions of the magic methods
print(repr(first_employee))
print(str(first_employee))
print("\n")
print(first_employee.__repr__())
print(first_employee.__str__())

print('\nPay amount of two employees: {}'.format(first_employee + second_employee))
print('\nThe length of the first employee\'s full name: ', len(first_employee))
