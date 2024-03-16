# https://leetcode.com/problems/modify-columns/description/
import pandas as pd

def multiplySalary(salary: int):
    return salary * 2

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'].apply(multiplySalary)
    return employees