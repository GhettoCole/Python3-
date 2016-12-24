import datetime


class Employee:

    # Class variables
    number_of_employees = 0
    raise_amt = 2.04

    # Initialising attributes of an instance
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@Gmail.com'

        # Increment a worker each time an instance is created for an object
        Employee.number_of_employees += 1

    # Defining a function for returning a concatenation of two instance attributes
    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    # Redefining the instance's attribute of pay each time the apply_raise function is called
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # A class method for allowing a class' variable to be redefined so one can call it without
    # the use of self.raise_amount
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # Using a class method as an alternative constructor
    # For returning the passed in arguments with a split dash(-) without the use of calling for self
    @classmethod
    def new_workers(cls, more_employees):
        first_name, last_name, pay = more_employees.split('-')
        return cls(first_name, last_name, pay)

    # Static methods don't operate on the class
    # Functions of the static methods can be called without reference of the class' initialization nor self
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


def date_check():
    print("Monday is a work day: ", end="")
    my_date = datetime.date(2016, 11, 28)
    print(Employee.is_workday(my_date))

date_check()


def main():
    employee_1 = Employee("Given", "Lepita", 3000)
    employee_2 = Employee("Thapelo", "Lepita", 3000)

    Employee.set_raise_amt(3.09)
    print("Employees raise amount is: ", Employee.raise_amt)
    # Using class methods as constructors
    employee_3 = 'Goitse-Lepita-7000'
    first_name, last_name, pay = employee_3.split('-')
    employee_3 = Employee(first_name, last_name, pay)
    print("\nNumber of employees: ", Employee.number_of_employees)
    print("\nEmployees: ")
    print("1 -\t{} {}".format(employee_1.last_name, employee_1.first_name))
    print("2 -\t{} {}".format(employee_2.last_name, employee_2.first_name))
    print("3 -\t{} {}".format(employee_3.last_name, employee_3.first_name))

    print("\nEmployee's Emails: ")
    print("1 -\t{}".format(employee_1.email))
    print("2 -\t{}".format(employee_2.email))
    print("3 -\t{}".format(employee_3.email))
    # Referencing the class method of the alternative constructor
    employee_4 = 'Retshidisitwe-Lepita-8600'
    employee_4 = Employee.new_workers(employee_4)
    print("\nA New intern: {} {}".format(employee_4.first_name, employee_4.last_name))

    print("\nUpdated Number of employees: ", Employee.number_of_employees)
    print("\nEmployees: ")
    print("1 -\t{} {}".format(employee_1.last_name, employee_1.first_name))
    print("2 -\t{} {}".format(employee_2.last_name, employee_2.first_name))
    print("3 -\t{} {}".format(employee_3.last_name, employee_3.first_name))
    print("4 -\t{} {}".format(employee_4.last_name, employee_4.first_name))
main()
