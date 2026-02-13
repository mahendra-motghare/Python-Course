#age & salary
from datetime import datetime

def calculate_age(birthdate):
    birth_year = int(birthdate.split('-')[-1])
    current_year = datetime.now().year
    return current_year - birth_year

def convert_salary_to_dollars(salary_in_rupees):
    int_to_usd = 0.012
    return salary_in_rupees * int_to_usd

birthdate = input()
salary_in_rupees = float(input())

age = calculate_age(birthdate)
salary_in_dollars = convert_salary_to_dollars(salary_in_rupees)

print(f"Age: {age}")
print(f"Salary in Dollars: {salary_in_dollars:.2f}")
