class Employee:
    "Common base class for all employees"

    empCount = 0  # Shared among all instances of the class

    # Constructor:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    # Class methods:
    # Note: Declaration needs first argument to be self

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)


employee1 = Employee("Alan", 5000000)
employee2 = Employee("Zelda", 12345)


employee1.displayEmployee()
employee2.displayEmployee()

print("Total employees %d" % Employee.empCount)

employee2.name = "Lara"
employee2.displayEmployee()

del employee2.salary
if hasattr(employee2, 'salary') == False:
    print(employee2.name, "doesn't have a salary")

    setattr(employee2, "salary", 54321)

    print(employee2.name, "salary is", getattr(employee2, "salary"))

delattr(employee2, "salary")
if hasattr(employee2, "salary") == False:
    print("Oops! We are not paying", employee2.name, "at all!")


print("\n+---------------------+\n|  Memory management  |\n+---------------------+\n")
print("No need to manage memory")


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")


pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))   # prints the ids of the obejcts
del pt1
del pt2
del pt3


print("\n+---------------+\n|  Inheritance  |\n+---------------+\n")


class Parent:        # define parent class
    parentAttr = 100

    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print('Calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attribute :", Parent.parentAttr)


class Child(Parent):  # define child class
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print('Calling child method')


c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method

print("\n+-------------------------+\n|  Overloading Operators  |\n+-------------------------+\n")


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)

# Vector (2, 10) + Vector (5, -2) = Vector (7, 8)
print(v1, "+", v2, "=", v1 + v2)


print("\n+---------------+\n|  Data Hiding  |\n+---------------+\n")


class JustCounter:
    __secretCount = 0  # Start with __ ("Double underscores") to hide

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
# print(counter.__secretCount)
print("Secrets: ", counter._JustCounter__secretCount)  # Acess hidden data
