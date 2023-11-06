import employee

while True:
    print("\n menu:")
    print("1. add employee")
    print("2. update employee")
    print("3. report")
    print("4. list all employee")
    print("5. exit")

    select=input("enter ur choice(1/2/3/4/5):")

    if select=="1":
        employee.add_employee()
    elif select=="2":
        employee.update_employee()
    elif select=="3":
        report= employee.report()
        if report:
            print(report)
        else:
            print("employee not found")
    elif select=="4":
        all_employee=employee.list_employee()
        print("\n all employee:")
        for employee in all_employee:
            print(f"id:{employee.employee_id}| name:{employee.name}| Position: {employee.position} | salary:${employee.salary}")
    elif select=="5":
        break
    else:
        print("invalid select")