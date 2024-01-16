import pandas as pd

# Importē funkcijas no fuknciju failiem
from funkcijas.avg_time import calculate_average_employment_time_for_divisions
from funkcijas.avg_salary import average_salary
from funkcijas.count_officials import count_officials
from funkcijas.count_employees import count_employees_per_division
from funkcijas.count_by_address import count_employees_by_address
from funkcijas.check_vacation import check_if_on_vacation
from funkcijas.check_replace import check_if_being_replaced
from funkcijas.empl_workload import count_employees_by_workload
from funkcijas.empl_eval import count_employee_evaluation
from funkcijas.empl_education import count_education_levels
from funkcijas.avg_evaluation_per_division import avg_evaluation_per_division

# Ielādē datus no Excel faila
df = pd.read_excel('empl.xlsx')
education_file_path = 'education.xlsx'

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

# Aprēķina darbinieku skaitu pēc adreses
address_counts = count_employees_by_address(df)

# Pārbauda, cik darbinieki ir atvaļinājumā
is_on_vacation = check_if_on_vacation(df)

# Pārbauda, cik darbinieki tiek aizvietoti
is_being_replaced = check_if_being_replaced(df)

# Cik darbinieku ir katrā slodzē
workload_counts = count_employees_by_workload(df)

# Cik darbinieku ir katrā vērtējumā
evaluation_counts = count_employee_evaluation(df)

# Cik darbinieku ir katrā izglītības līmenī
education_counts = count_education_levels(education_file_path)

# Vidējais vērtējums katrā nodaļā
division_avg_evaluations = avg_evaluation_per_division(df, division_list)

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
# print("---------------------------------------------")
# print(f"{officials_counts['amatpersonas']} darbinieki ir amatpersonas.")
# print(f"{officials_counts['nav amatpersonas']} darbinieki nav amatpersonas.")
# print("---------------------------------------------")
for address, count in address_counts.items():
    print(f"Adresē '{address}' strādā {count} darbinieki.")
print("---------------------------------------------")
print(f"{is_on_vacation.sum()} darbinieki ir atvaļinājumā.")
print(f"{is_being_replaced.sum()} darbinieki tiek aizvietoti.")
print("---------------------------------------------")
for workload, count in workload_counts.items():
    print(f"Slodze {workload} - {count} darbinieki")
print("---------------------------------------------")
for evaluation, count in evaluation_counts.items():
    print(f"Vērtējums {evaluation} - {count} darbinieki")
print("---------------------------------------------")
print("Izglītības līmeņi:")
for education, count in education_counts.items():
    print(f"{education} - {count} darbinieki")
print("---------------------------------------------")
print("Vidējais novērtējums katrā nodaļā:")
for division, avg_evaluation in division_avg_evaluations.items():
    if pd.isna(avg_evaluation):
        print(f"{division}: Nav pietiekami datu")
    else:
        print(f"{division}: {avg_evaluation:.2f}")