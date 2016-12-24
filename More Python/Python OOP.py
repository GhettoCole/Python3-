class Employee:
    # Initialize class' attributes
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@Gmail.com'

    def fullname(self):
        return "{} {}".format(self.first, self.last)


def main():
    given = Employee('Given', 'Lepita', 9000)
    lepita = Employee('GhettoCole', 'Ashtray', 800)

    print(given.fullname())
    print(lepita.fullname())
    # Another way of accessing an employee's attribute
    print(Employee.fullname(given))


main()
