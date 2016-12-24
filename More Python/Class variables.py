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


def main():
    given = Employee('Given', 'Lepita', 9000)
    lepita = Employee('GhettoCole', 'Ashtray', 800)

    print("Before a raise: ", given.pay)
    print("Before a raise: ", lepita.pay)
    given.apply_raise()
    lepita.apply_raise()
    print("\nAfter a raise: ", given.pay)
    print("After a raise: ", lepita.pay)

    print('\n')
    print(given.__dict__)
    print(lepita.__dict__)
    Employee.raise_amount = 2.09

    print("\nBefore a raise: ", given.pay)
    print("Before a raise: ", lepita.pay)
    given.apply_raise()
    lepita.apply_raise()
    print("\nAfter a raise: ", given.pay)
    print("After a raise: ", lepita.pay)
    print('\n')
    given.raise_amount = 2.99
    print(given.__dict__)

    print("\nThe number of employees: ", Employee.number_of_employees)

    remo = Employee("Remoneilwe", "Magdeline", 9700)
    print("New employee's name: {}".format(remo.first))
    print("\nThe number of employees: ", Employee.number_of_employees)


main()
