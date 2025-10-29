employees = []

def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("         EMPLOYEE MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")
    print("="*50)

def get_next_employee_id(employees):
    """Generate next available employee ID"""
    if not employees:
        return 1
    return max(emp["id"] for emp in employees) + 1

def add_employee(employees):
    """Add a new employee to the system"""
    print("\n--- Add New Employee ---")
    
    if len(employees) >= 8:
        print(" Maximum employee limit reached (8 employees)")
        print("Please delete an employee before adding a new one.")
        return employees
    
    try:
        print(f"Employee ID will be auto-generated: {get_next_employee_id(employees)}")
        name = input("Enter employee name: ").strip()
        if not name:
            print(" Name cannot be empty")
            return employees
            
        department = input("Enter department: ").strip()
        if not department:
            print(" Department cannot be empty")
            return employees
            
        role = input("Enter role: ").strip()
        if not role:
            print(" Role cannot be empty")
            return employees
            
        salary = float(input("Enter salary: ₹"))
        if salary <= 0:
            print(" Salary must be positive")
            return employees
            
    except ValueError:
        print(" Invalid salary format. Please enter a valid number.")
        return employees
    
    new_employee = {
        "id": get_next_employee_id(employees),
        "name": name,
        "department": department,
        "role": role,
        "salary": salary
    }
    
    employees.append(new_employee)
    print(f" Employee '{name}' added successfully!")
    print(f" Total employees: {len(employees)}/8")
    
    return employees

def view_employees(employees):
    """Display all employees in tabular format"""
    print("\n--- All Employees ---")
    
    if not employees:
        print(" No employees found in the system")
        return
    
    print("\n" + "="*80)
    print(f"{'ID':<5} {'Name':<15} {'Department':<12} {'Role':<15} {'Salary':<10}")
    print("-" * 80)
    
    for emp in employees:
        print(f"{emp['id']:<5} {emp['name']:<15} {emp['department']:<12} {emp['role']:<15} ₹{emp['salary']:<8}")
    
    print("=" * 80)
    print(f" Total Employees: {len(employees)}/8")

def search_employee(employees):
    """Search employee by ID or Name"""
    print("\n--- Search Employee ---")
    
    if not employees:
        print(" No employees to search")
        return
    
    print("Search by:")
    print("1. Employee ID")
    print("2. Employee Name")
    
    try:
        search_type = int(input("Enter your choice (1-2): "))
    except ValueError:
        print(" Please enter a valid number")
        return
    
    if search_type == 1:
        try:
            emp_id = int(input("Enter employee ID: "))
        except ValueError:
            print(" Please enter a valid ID number")
            return
        
        found = False
        for emp in employees:
            if emp["id"] == emp_id:
                print("\n Employee Found:")
                print("-" * 50)
                print(f"ID: {emp['id']}")
                print(f"Name: {emp['name']}")
                print(f"Department: {emp['department']}")
                print(f"Role: {emp['role']}")
                print(f"Salary: ₹{emp['salary']}")
                print("-" * 50)
                found = True
                break
        
        if not found:
            print(" Employee not found with the given ID")
    
    elif search_type == 2:
        name = input("Enter employee name: ").strip().lower()
        
        found_employees = [emp for emp in employees if name in emp["name"].lower()]
        
        if found_employees:
            print(f"\n Found {len(found_employees)} employee(s):")
            print("=" * 60)
            for emp in found_employees:
                print(f"ID: {emp['id']}, Name: {emp['name']}, Department: {emp['department']}, Role: {emp['role']}")
            print("=" * 60)
        else:
            print(" No employees found with the given name")
    
    else:
        print(" Invalid choice. Please select 1 or 2")

def update_employee(employees):
    """Update employee details"""
    print("\n--- Update Employee ---")
    
    if not employees:
        print(" No employees to update")
        return employees
    
    view_employees(employees)
    
    try:
        emp_id = int(input("\nEnter employee ID to update: "))
    except ValueError:
        print(" Please enter a valid ID number")
        return employees
    
    employee_to_update = None
    for emp in employees:
        if emp["id"] == emp_id:
            employee_to_update = emp
            break
    
    if not employee_to_update:
        print(" Employee not found with the given ID")
        return employees
    
    print(f"\nCurrent details of {employee_to_update['name']}:")
    print(f"1. Department: {employee_to_update['department']}")
    print(f"2. Role: {employee_to_update['role']}")
    print(f"3. Salary: ₹{employee_to_update['salary']}")
    
    print("\nWhat would you like to update?")
    print("1. Department")
    print("2. Role")
    print("3. Salary")
    print("4. Cancel update")
    
    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print(" Please enter a valid number")
        return employees
    
    if choice == 1:
        new_department = input("Enter new department: ").strip()
        if new_department:
            employee_to_update["department"] = new_department
            print(" Department updated successfully!")
        else:
            print(" Department cannot be empty")
    
    elif choice == 2:
        new_role = input("Enter new role: ").strip()
        if new_role:
            employee_to_update["role"] = new_role
            print(" Role updated successfully!")
        else:
            print(" Role cannot be empty")
    
    elif choice == 3:
        try:
            new_salary = float(input("Enter new salary: ₹"))
            if new_salary > 0:
                employee_to_update["salary"] = new_salary
                print(" Salary updated successfully!")
            else:
                print(" Salary must be positive")
        except ValueError:
            print(" Please enter a valid salary amount")
    
    elif choice == 4:
        print(" Update cancelled")
    
    else:
        print(" Invalid choice")
    
    return employees

def delete_employee(employees):
    """Delete an employee by ID"""
    print("\n--- Delete Employee ---")
    
    if not employees:
        print(" No employees to delete")
        return employees
    
    view_employees(employees)
    
    try:
        emp_id = int(input("\nEnter employee ID to delete: "))
    except ValueError:
        print(" Please enter a valid ID number")
        return employees
    
    employee_to_delete = None
    for emp in employees:
        if emp["id"] == emp_id:
            employee_to_delete = emp
            break
    
    if not employee_to_delete:
        print(" Employee not found with the given ID")
        return employees
    
    print(f"\n  Are you sure you want to delete {employee_to_delete['name']} (ID: {employee_to_delete['id']})?")
    confirmation = input("Type 'YES' to confirm deletion: ").strip().upper()
    
    if confirmation == "YES":
        employees = [emp for emp in employees if emp["id"] != emp_id]
        print(f" Employee '{employee_to_delete['name']}' deleted successfully!")
        print(f" Remaining employees: {len(employees)}/8")
    else:
        print(" Deletion cancelled")
    
    return employees

def add_sample_data(employees):
    """Add sample data for testing"""
    sample_employees = [
        {"id": 1, "name": "Alice Johnson", "department": "HR", "role": "Manager", "salary": 50000},
        {"id": 2, "name": "Bob Smith", "department": "IT", "role": "Developer", "salary": 60000},
        {"id": 3, "name": "Carol Davis", "department": "Finance", "role": "Analyst", "salary": 55000}
    ]
    
    for emp in sample_employees:
        if len(employees) < 8:
            employees.append(emp)
    
    print(" Sample data added for testing")
    return employees

def menu():
    """Main menu function to handle user interactions"""
    global employees
    
    
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print(" Please enter a valid number (1-6)")
            continue
        
        if choice == 1:
            employees = add_employee(employees)
        
        elif choice == 2:
            view_employees(employees)
        
        elif choice == 3:
            search_employee(employees)
        
        elif choice == 4:
            employees = update_employee(employees)
        
        elif choice == 5:
            employees = delete_employee(employees)
        
        elif choice == 6:
            print("\n Thank you for using Employee Management System!")
            print(" Final employee count:", len(employees))
            print("Goodbye! ")
            break
        
        else:
            print(" Invalid choice. Please select 1-6")

if __name__ == "__main__":
    print(" Employee Management System")
    print(" Maximum capacity: 8 employees")
    print(" No data persistence - all data lost on exit")
    
    menu()