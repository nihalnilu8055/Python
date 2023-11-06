class Employee:
    def __init__(self,employee_id,name,position,salary):
        self.employee_id=employee_id
        self.name=name
        self.position=position
        self.salary=salary

employee_list=[]

def add_employee():
    employee_id=int(input("enter employee id: "))
    name=input("enter employee name: ")
    position=input("enter employee position: ")
    salary=float(input("enter employee salary: "))

    employee=Employee(employee_id,name,position,salary)
    employee_list.append(employee)
    print(f"Employee {name} has been added with ID {employee_id}")

def update_employee():
    employee_id=input("enter employee id to update: ")
    for employee in employee_list:
        if employee.employee_id ==employee_id:
            name=input("enter updated name (current:{employee.name}):")
            position=input(f"enter updated postion (current:{employee.position}):")
            salary=input(f"enter updated salary (current:{employee.salary}):")

            if name:
                employee.name=name
            if position:
                employee.position=position
            if salary:
                employee.salary=float(salary)
            
            print(f"employee with id {employee_id} does not exist")

def report():
    employee_id=input("enter employee id to generate report: ")
    for employee in employee_list:
        if employee.employee_id ==employee_id:
            report=f"employee id:{employee.employee_id}\n"
            report+=f"name:{employee.name}\n"
            report+=f"position:{employee.position}\n"
            report+=f"salary:${employee.salary}"
            return report
        else:
            return f"employee with id {employee_id} does not exist"

def list_employee():
    return employee_list