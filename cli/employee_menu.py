from services.auth import EmployeeAuthentication
from repositories.employee_repo import EmployeeDb

#this object of employee repo
emp_db = EmployeeDb()
#this is object of employee auth
emp_auth = EmployeeAuthentication(emp_db)


#this function for signup new employee
def employeeSignup():
    print('Employee Signup')
    name = input('Enter your name:')
    email = input('Enter your email:')
    password = input('Enter your password:')
    emp_auth.createEmployee(name,email,password)

def employeeLogin():
    print('Employee Login')