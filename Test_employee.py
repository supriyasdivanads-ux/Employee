#test_employee.py
import pytest
from employee import employee_details 

def test_employee_details():
    #Sample data
    name = "Alice Smith"
    emp_id = "E202"
    department = "HR"
    salary = 60000
    #Expected result
    expected_output = (
         f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )
        
    #Assertion
    assert  employee_details (name,emp_id,department,salary) == expected_output