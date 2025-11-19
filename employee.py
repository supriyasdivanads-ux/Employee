def employee_details(name, emp_id, department, salary):
    formatted_output = (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )
    return formatted_output


def main():
    # Direct values (no input taken)
    name = "John Doe"
    emp_id = 101
    department = "HR"
    salary = 50000

    # Calling the function
    print(employee_details(name, emp_id, department, salary))


# Entry point
if __name__ == "__main__":
    main()