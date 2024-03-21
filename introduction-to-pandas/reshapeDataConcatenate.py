# https://leetcode.com/problems/reshape-data-concatenate/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2])