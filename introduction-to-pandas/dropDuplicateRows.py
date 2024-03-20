# https://leetcode.com/problems/drop-duplicate-rows/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers = customers.drop_duplicates(subset=['email'], keep='first')
    return customers