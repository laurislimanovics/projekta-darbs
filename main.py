import pandas as pd

# Importē funkcijas no fuknciju failiem
from funkcijas.avg_time import calculate_average_employment_time_for_divisions
from funkcijas.avg_salary import average_salary
from funkcijas.count_officials import count_officials
from funkcijas.count_employees import count_employees_per_division

# Ielādē datus no Excel faila
df = pd.read_excel('empl.xlsx')

# Nodaļu saraksts
division_list = ['Jelgavas reģionālā nodaļa', 'Daugavpils reģionālā nodaļa', 'Valmieras reģionālā nodaļa', 'Ventspils reģionālā nodaļa', 'Liepājas reģionālā nodaļa', 
                 'Rēzeknes reģionālā nodaļa', 'Rīgas pilsētas Zemgales nodaļa', 'Rīgas pilsētas Latgales nodaļa', 'Pārvaldes struktūrvienības', 'Starptautisko pakalpojumu nodaļa', 
                 'Informācijas apstrādes nodaļa', 'Iemaksu nodaļa', 'Slepenības režīma nodrošināšanas nodaļa']


# Aprēķina darbinieku skaitu katrā nodaļā
division_employee_counts = count_employees_per_division(division_list, df)

# Aprēķina vidējo algu nodaļām
division_salary_averages = average_salary(division_list, df)

# Aprēķina vidējo darba stāžu nodaļām
division_averages = calculate_average_employment_time_for_divisions(division_list, df)

# Aprēķina amatpersonu skaitu
officials_counts = count_officials(df)

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
print("---------------------------------------------")
print(f"{officials_counts['amatpersonas']} darbinieki ir amatpersonas.")
print(f"{officials_counts['nav amatpersonas']} darbinieki nav amatpersonas.")