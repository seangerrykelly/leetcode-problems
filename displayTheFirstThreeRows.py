# https://leetcode.com/problems/display-the-first-three-rows/description/
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.iloc[0:3]
    