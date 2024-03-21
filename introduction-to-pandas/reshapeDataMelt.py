# https://leetcode.com/problems/reshape-data-melt/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    report = report.melt(id_vars=['product'], value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'], var_name='quarter')
    report = report.rename(columns={'value':'sales'})
    return report