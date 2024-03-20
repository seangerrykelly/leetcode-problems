# https://leetcode.com/problems/drop-missing-data/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students = students.dropna(subset=['name'])
    return students