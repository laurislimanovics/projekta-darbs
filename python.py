import pandas as pd

# Ielādē datus no Excel faila
df = pd.read_excel('empl.xlsx')

# Nodaļu saraksts
division_list = ['Jelgavas reģionālā nodaļa', 'Daugavpils reģionālā nodaļa', 'Valmieras reģionālā nodaļa', 'Ventspils reģionālā nodaļa', 'Liepājas reģionālā nodaļa', 'Rēzeknes reģionālā nodaļa', 'Rīgas pilsētas Zemgales nodaļa', 'Rīgas pilsētas Latgales nodaļa', 'Pārvaldes struktūrvienība', 'Starptautisko pakalpojumu nodaļa', 'Iemaksu nodaļa', 'Informācijas apstrādes nodaļa', 'Iemaksu nodaļa', 'Slepenības režīma nodrošināšanas nodaļa']

# Funkcija, kas aprēķina vidējo darba stāžu nodaļām
def calculate_average_employment_time_for_divisions(divisions, dataframe):
    average_times = {}
    
    for division in divisions:
        division_df = dataframe[dataframe['Pilns nosaukums'] == division]
        
        # aprēķina vidējo darba stāžu
        average_time = division_df['Iestādes stāžs'].mean()
        
        average_times[division] = average_time
    
    return average_times

# Aprēķina vidējo darba stāžu nodaļām
division_averages = calculate_average_employment_time_for_divisions(division_list, df)

# Izvada rezultātus
for division, average_time in division_averages.items():
    print(f"{division}  -  vidējais darba stāžs: {average_time:.2f} gadi")
