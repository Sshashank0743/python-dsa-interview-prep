class Employee:

    def __init__(self, name, emp_id, email_id, phone):
        self.name = name
        self.emp_id = emp_id
        self.email_id = email_id
        self.phone = phone

    def get_name(self):
        return self.name

    def get_emp_id(self):
        return self.emp_id

    def get_email_id(self):
        return self.email_id

    def get_phone(self):
        return self.phone
    
class OrganizationDirectory:

    def __init__(self, emp_list):
        self.__emp_list = emp_list

    def lookup(self,key_name, key_emp_id):
        result_list=[]
        for emp in self.__emp_list:
            if(key_name in emp.get_name()):
                result_list.append(emp)
            if(key_emp_id in emp.get_emp_id()):
                result_list.append(emp)
        self.display(result_list)
        return result_list

    def display(self,result_list):
        print("Search results:")
        for emp in result_list:
            print(emp.get_name()," ", 
                  emp.get_emp_id()," ",
                  emp.get_email_id(), " ",
                  emp.get_phone())


emp1=Employee("Kevin",24089, "Kevin_xyz@organization.com", 9874563210)
emp2=Employee("Jack",56789,"Jack_xyz@organization.com", 9874563210)
emp3=Employee("Jackson",67895,"Jackson_xyz@organization.com", 9874563210)
emp4=Employee("Henry Jack",23456,"Jacky_xyz@organization.com", 9874563210)
emp5=Employee("Kevin Jack",159636,"Jacky_abc@organization.com", 9874562210)
emp_list=[emp1,emp2,emp3,emp4,emp5]

org_dir=OrganizationDirectory(emp_list)
#Search for an employee
org_dir.lookup("")
org_dir.lookup("56789")

    