import pandas as pd

def calculate_average_employment_time_for_divisions(divisions, dataframe):
    average_times = {}
    for division in divisions:
        # Tiek izmantota funkcija str.contains, lai atrastu rindas, kurās ir minēta nodaļa
        division_df = dataframe[dataframe['Pilns nosaukums'].str.contains(division, na=False, regex=False)]
        # Aprēķina vidējo darba stāžu
        average_time = division_df['Iestādes stāžs'].mean()
        average_times[division] = average_time
    return average_times