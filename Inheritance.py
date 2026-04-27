"""
class Employee:
    def __init__(self):
        self.name='Fzee'
        self.designation='Developer'
                                        # One parent-One child - Single Inheritance
class Developer(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.language='Python'
        self.Qualification='Software Engineer'
    def work(self):
        print(f"{self.name} Developing new Software")


emp=Developer()
emp.work()
"""


"""class Employee:
    def __init__(self, n, des):
        self.name=n
        self.designation=des
                                        # One parent-One child - Single Inheritance
class Developer(Employee):
    def __init__(self,n,des,lan,qual):
        Employee.__init__(self,n,des)   #Super().__init__(n,des)
        self.language=lan
        self.Qualification=qual
    def work(self):
        print(f"{self.name} Developing new Software. He is a {self.Qualification}")

                                        #Heirarchical Inheritance - One Parent - Many Child
emp=Developer("Fzee","Developer","Python","Software Engineer")
emp.work()
"""
#Multiple Inheritance

class Employee:
    def set_employee(self, name, salary):
        self.name = name
        self.salary = salary

    def show_employee(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class HR:
    def hire(self):
        print("Hiring new employees")

    def fire(self):
        print("Removing an employee")

class Manager(Employee, HR):
    m1 = Manager()
m1.set_employee("Rahul", 50000)

m1.show_employee()   # from Employee
m1.hire()            # from HR
m1.fire()            # from HR
