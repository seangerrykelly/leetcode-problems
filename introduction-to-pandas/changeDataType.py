# https://leetcode.com/problems/change-data-type/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd

def convertGradeToInt(grade: float) -> int:
    return int(grade)

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].apply(convertGradeToInt)
    return students