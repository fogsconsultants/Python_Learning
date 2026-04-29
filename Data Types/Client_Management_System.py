"""class client:
    def __init__(self,customer_name,company,service_type):
        self.client_name=customer_name
        self.company=company
        self.service_type=service_type
    def display(self):
        print("client_name:",self.client_name)
        print("company name:", self.company)
        print("Service type:",self.service_type)
class PremiumClient(client):
    def __init__(self,customer_name,company,service_type,p_support):
        super().__init__(customer_name,company,service_type)
        self.priority_support=p_support
cl1=PremiumClient("Ebin","One Team","Resume", False)
cl1.display()
"""
"""class employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary
    def display(self):
        print("employee name:",self.name)
        print("employee_designation:",self.role)
        print("employee_salary:",self.salary)
class recruiter(employee):
    def __init__(self, name, role, salary, clients_handled):
        super().__init__(name,role,salary)
        self.clients_handled=clients_handled
    def display(self):
        super().display()
        print("clients_handled:", self.clients_handled)
class SalesHead(employee):
    def __init__(self,name,role,salary,region):
        super().__init__(name,role,salary)
        self.region=region
    def display(self):
        super().display()
        print("Region:", self.region)

recruiter1=recruiter("Raju", "Recruiter", 50000, 100)
Sales1=SalesHead("Radha", "Sales Head", 200000, "Kerala")

recruiter1.display()
print('-------------------')
Sales1.display()
"""

class Job:
    def __init__(self, job_title, company, salary):
        self.job_title=job_title
        self.company=company
        self.salary=salary
    def display(self):
        print("job_title:",self.job_title)
        print("company", self.company)
        print("salary", self.salary)
job1 = Job("HR Manager", "Infosys", 100000)
job2 = Job("Sales Manager", "Risto Solar", 80000)
job3 = Job("Sales Engineer", "Fogs Developers", 50000)

job1.display()
print("----------")
job2.display()
print("----------")
job3.display()

class RemoteJob(Job):
    def __init__(self, job_title, company, salary, work_from_home):
        super().__init__(job_title, company, salary)
        self.work_from_home=work_from_home
    def display(self):
        super().display()
        print("work_from_home:", self.work_from_home, True)

        
class OnsiteJob(Job):
    def __init__(self, job_title, company, salary, onsite_job):
        super().__init__(job_title, company, salary)
        self.onsite_job=onsite_job
    def display(self):
        super().display()
        print("onsite_job:", self.onsite_job)

