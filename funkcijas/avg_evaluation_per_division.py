import pandas as pd

def avg_evaluation_per_division(dataframe, divisions):
    grade_to_numeric = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'F': 1}
    dataframe['NumericVērtējums'] = dataframe['Vērtējums'].map(grade_to_numeric)

    average_evaluations = {}
    for division in divisions:
        division_df = dataframe[dataframe['Pilns nosaukums'].str.contains(division, na=False, regex=False)]
        if not division_df.empty:
            average_evaluation = round(division_df['NumericVērtējums'].mean(), 2)
            average_evaluations[division] = average_evaluation

    return average_evaluations