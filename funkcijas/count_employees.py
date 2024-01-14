import pandas as pd

def count_employees_per_division(divisions, dataframe):
    employee_counts = {}
    for division in divisions:
        # Tiek izmantota funkcija str.contains, lai atrastu rindas, kurās ir minēta nodaļa
        division_df = dataframe[dataframe['Pilns nosaukums'].str.contains(division, na=False, regex=False)]
        # Skaita rindas, kas atbilst nodaļai
        employee_count = len(division_df)
        employee_counts[division] = employee_count
    return employee_counts