class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print
        "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print
        "Name : ", self.name, ", Salary: ", self.salary

    def printme(str):
        "This prints a passed string into this function"
        print(str)

        return