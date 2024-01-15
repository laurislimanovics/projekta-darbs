import pandas as pd

def count_employee_evaluation(dataframe):
    evaluation_counts = dataframe['Vērtējums'].value_counts()
    evaluation_counts['Nav novērtēts'] = dataframe['Vērtējums'].isna().sum()
    return evaluation_counts