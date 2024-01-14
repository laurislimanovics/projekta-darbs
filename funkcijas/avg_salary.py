import pandas as pd

def average_salary(divisions, dataframe):
    average_salaries = {}
    for division in divisions:
        # Tiek izmantota funkcija str.contains, lai atrastu rindas, kurās ir minēta nodaļa
        division_df = dataframe[dataframe['Pilns nosaukums'].str.contains(division, na=False, regex=False)]
        # Aprēķina vidējo algu
        average_salary = division_df['Alga'].mean()
        average_salaries[division] = average_salary
    return average_salaries