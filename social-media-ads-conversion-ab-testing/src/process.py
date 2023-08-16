import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.impute import KNNImputer


def data_overview(data: pd.DataFrame) -> None:
    # print('1. Data description: ')
    # print(df.describe(include='all'))  # Description of dataset
    print(f'1. Shape of dataset: {data.shape}')
    print('2. Columns datatype: ')
    for group, column in data.columns.to_series().groupby(data.dtypes):  # Datatype of each column
        print(group, end='\t| ')
        for name in column:
            print(name, end=', ')
        print()


def check_missing_data(data: pd.DataFrame) -> pd.Series:
    """Check for missing data in the df (display in descending order)"""
    result = ((data.isnull().sum() * 100) /
              len(data)).sort_values(ascending=False)
    return result
