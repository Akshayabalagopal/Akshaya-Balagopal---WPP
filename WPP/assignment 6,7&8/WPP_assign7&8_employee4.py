'''Create a class "Employee" with attributes name and salary. Implement overloaded operators +
and - to combine and compare employees based on their salaries.
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        
        if isinstance(other, Employee):
            combined_salary = self.salary + other.salary
            return Employee(f"{self.name} & {other.name}", combined_salary)
        return NotImplemented

    def __sub__(self, other):
        
        if isinstance(other, Employee):
            salary_difference = abs(self.salary - other.salary)
            return salary_difference
        return NotImplemented

    def __str__(self):
        
        return f"Employee: {self.name}, Salary: {self.salary}"

def main():
    employees = []

    num_employees = int(input("Enter no of employees: "))
    for i in range(num_employees):
        name = input(f"Enter the name of employee {i+1}: ")
        salary = float(input(f"Enter the salary of {name}: "))
        employees.append(Employee(name, salary))

    print("\nAll Employees:")
    for emp in employees:
        print(emp)

    combined_emp = employees[0]
    for emp in employees[1:]:
        combined_emp = combined_emp + emp

    print(f"\nCombined Employee from all: {combined_emp}")

    for emp in employees[1:]:
        salary_diff = employees[0] - emp
        print(f"Salary difference between {employees[0].name} and {emp.name}: {salary_diff}")

if __name__ == "__main__":
    main()
