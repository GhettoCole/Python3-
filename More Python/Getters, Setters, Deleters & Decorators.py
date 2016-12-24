class Employee:
    # Creating a class variable
    number_of_employees = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

        # Increment the value of employees each time an instance is created
        Employee.number_of_employees += 1

    @property
    def email(self):
        return "{}.{}@Gmail.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    # defining a setter
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("The fullname has successfully been deleted!")
        self.last = None
        self.first = None

# Using a setter to access the attributes of an instance

emp_1 = Employee('Given', 'Joy')
print("First name: {}".format(emp_1.first))
print("Last name: {}".format(emp_1.last))
print("Email address: {}".format(emp_1.email))
print("Full name: {}".format(emp_1.fullname))
print("\nDetails After Update\n")
emp_1.fullname = 'Given Lepita'
print("First name: {}".format(emp_1.first))
print("Last name: {}".format(emp_1.last))
print("Email address: {}".format(emp_1.email))
print("Full name: {}".format(emp_1.fullname))  # Using the property decorator to call the method as an attribute
del emp_1.fullname
