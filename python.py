import pandas as pd

# Ielādē datus no Excel faila
df = pd.read_excel('empl.xlsx')

# Nodaļu saraksts
division_list = ['Jelgavas reģionālā nodaļa', 'Daugavpils reģionālā nodaļa', 'Valmieras reģionālā nodaļa', 'Ventspils reģionālā nodaļa', 'Liepājas reģionālā nodaļa', 
                 'Rēzeknes reģionālā nodaļa', 'Rīgas pilsētas Zemgales nodaļa', 'Rīgas pilsētas Latgales nodaļa', 'Pārvaldes struktūrvienības', 'Starptautisko pakalpojumu nodaļa', 
                 'Informācijas apstrādes nodaļa', 'Iemaksu nodaļa', 'Slepenības režīma nodrošināšanas nodaļa']

# Funkcija, kas aprēķina vidējo darba stāžu nodaļām
def calculate_average_employment_time_for_divisions(divisions, dataframe):
    average_times = {}
    for division in divisions:
        # Tiek izmantota funkcija str.contains, lai atrastu rindas, kurās ir minēta nodaļa
        division_df = dataframe[dataframe['Pilns nosaukums'].str.contains(division, na=False, regex=False)]
        # Aprēķina vidējo darba stāžu
        average_time = division_df['Iestādes stāžs'].mean()
        average_times[division] = average_time
    return average_times

def average_salary(divisions, dataframe):
    average_salaries = {}
    for division in divisions:
        # Tiek izmantota funkcija str.contains, lai atrastu rindas, kurās ir minēta nodaļa
        division_df = dataframe[dataframe['Pilns nosaukums'].str.contains(division, na=False, regex=False)]
        # Aprēķina vidējo algu
        average_salary = division_df['Alga'].mean()
        average_salaries[division] = average_salary
    return average_salaries

def count_officials(dataframe, column_name='Amatpersona'):
    # Izmanto value_counts(), lai iegūtu skaitu katram unikālam ierakstam kolonnā
    counts = dataframe[column_name].value_counts()
    
    # Izvada rezultātus
    for value, count in counts.items():
        status = 'amatpersonas' if value else 'nav amatpersonas'
        print(f"{count} darbinieki ir {status}.")
# Funkcija, kas aprēķina darbinieku skaitu katrā nodaļā
def count_employees_per_division(divisions, dataframe):
    employee_counts = {}
    for division in divisions:
        # Tiek izmantota funkcija str.contains, lai atrastu rindas, kurās ir minēta nodaļa
        division_df = dataframe[dataframe['Pilns nosaukums'].str.contains(division, na=False, regex=False)]
        # Skaita rindas, kas atbilst nodaļai
        employee_count = len(division_df)
        employee_counts[division] = employee_count
    return employee_counts

# Funkcija, kas aprēķina darbinieku skaitu katrā nodaļā
def count_employees_per_division(divisions, dataframe):
    employee_counts = {}
    for division in divisions:
        # Tiek izmantota funkcija str.contains, lai atrastu rindas, kurās ir minēta nodaļa
        division_df = dataframe[dataframe['Pilns nosaukums'].str.contains(division, na=False, regex=False)]
        # Skaita rindas, kas atbilst nodaļai
        employee_count = len(division_df)
        employee_counts[division] = employee_count
    return employee_counts

# Aprēķina darbinieku skaitu katrā nodaļā
division_employee_counts = count_employees_per_division(division_list, df)

# Aprēķina vidējo algu nodaļām
division_salary_averages = average_salary(division_list, df)

# Aprēķina vidējo darba stāžu nodaļām
division_averages = calculate_average_employment_time_for_divisions(division_list, df)

# Aprēķina amatpersonu skaitu
count_officials(df)

# Izvada rezultātus
print("---------------------------------------------")
for division, average_time in division_averages.items():
    print(f"{division} - vidējais darba stāžs: {average_time:.2f} gadi")
print("---------------------------------------------")
for division, average_salary in division_salary_averages.items():
    print(f"{division} - vidējā alga: {average_salary:.2f} EUR")
print("---------------------------------------------")
for division, employee_count in division_employee_counts.items():
    print(f"{division} - darbinieku skaits: {employee_count}")
