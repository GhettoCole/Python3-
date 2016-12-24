class Employee:
    # Creating a class variables
    raise_amt = 1.04
    number_of_employees = 0

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@Gmail.com'

        Employee.number_of_employees += 1

    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

# The Developers subclass will have all attributes and method of the super class, without specification


class Developers(Employee):
    raise_amt = 1.10  # Increasing the developer's raise without affecting the super class

    def __init__(self, first_name, last_name, pay, pro_lang):
        super().__init__(first_name, last_name, pay)  # Allowing the superclass to handle the passed in arguments
        # Alternative for letting the super class initialize the passed in arguments of the Developers sub class
        Employee.__init__(self, first_name, last_name, pay)
        self.pro_lang = pro_lang


class Manager(Employee):
    def __init__(self, first_name, last_name, pay, employees=None):
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def show_employees(self):
        for employee in self.employees:
            print("--> ", employee.fullname())


def main():
    employee_1 = Employee("Goitse", "Lepita", 20000)
    employee_3 = Employee("Thapelo", "Lepita", 30000)
    developer_1 = Developers("Given", "Lepita", 50000, "Python Programming Language")

    print("A Python's Developer Pay Amount is ${}".format(developer_1.pay))

    developer_1.apply_raise()

    print("A Python's Developer Pay Amount After a Raise is ${}".format(developer_1.pay))

    print("A Developer's Pay Amount is ${}".format(employee_1.pay))

    employee_1.apply_raise()

    print("A Developer's Pay Amount After a Raise is ${}".format(employee_1.pay))

    manager_1 = Manager('Jordan', 'Rutherford', 90000, [developer_1])

    print("The managers email address: {}".format(manager_1.email))

    manager_1.add_employee(employee_3)

    manager_1.add_employee(employee_1)

    print("{} {} employees: ".format(manager_1.first_name, manager_1.last_name))

    manager_1.show_employees()

    manager_1.remove_employee(developer_1)

    print("{} {} employees After An Update: ".format(manager_1.first_name, manager_1.last_name))
    manager_1.show_employees()
    print("\nIs manager 1 an instance of a subclass 'Manager': ", isinstance(manager_1, Manager))
    print("\nIs manager 1 an instance of a superclass 'Employee': ", isinstance(manager_1, Employee))
    print("\nIs manager 1 an instance of a subclass 'Developers': ", isinstance(manager_1, Developers))

    print("\nIs Developers a subclass of Employee: ", issubclass(Developers, Employee))
    print("\nIs Manager a subclass of Employee: ", issubclass(Manager, Employee))
    print("\nIs Developers a subclass of Manager: ", issubclass(Developers, Manager))
    print("\nIs Manager a subclass of Developers: ", issubclass(Manager, Developers))

main()
# The issubclass function tells us if a class is a subclass of another class
# The isinstance function tells us if an object is an instance of a class
# Getting help on a subclass to see the inherited attributes and methods

# print(help(Developers))
