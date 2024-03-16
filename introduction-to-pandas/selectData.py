# https://leetcode.com/problems/select-data/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    student = students.loc[students['student_id'] == 101, ['name', 'age']]
    return student