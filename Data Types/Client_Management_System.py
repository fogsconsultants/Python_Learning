class client:
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
