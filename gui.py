import tkinter as tk
import pandas as pd
from tkinter import ttk

# Ifunktiju importēšana
from funkcijas.avg_salary import average_salary
# vieta pērējām funkcijām

# Nolasa datus no faila
df = pd.read_excel('empl.xlsx')

division_list = ['Jelgavas reģionālā nodaļa', 'Daugavpils reģionālā nodaļa', 'Valmieras reģionālā nodaļa', 'Ventspils reģionālā nodaļa', 'Liepājas reģionālā nodaļa', 
                 'Rēzeknes reģionālā nodaļa', 'Rīgas pilsētas Zemgales nodaļa', 'Rīgas pilsētas Latgales nodaļa', 'Pārvaldes struktūrvienības', 'Starptautisko pakalpojumu nodaļa', 
                 'Informācijas apstrādes nodaļa', 'Iemaksu nodaļa', 'Slepenības režīma nodrošināšanas nodaļa']


def generate_report():
    # dabū izvēlēto report_type
    report_type = report_type_var.get()
    # izsauc atbilstošo funkciju
    if report_type == 'Average Salary':
        result = average_salary(division_list, df)
    # parāda rezultātu
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, str(result))

# izveido GUI
root = tk.Tk()

# Dropdown izvēlei
report_type_var = tk.StringVar()
report_type_dropdown = ttk.Combobox(root, textvariable=report_type_var)
report_type_dropdown['values'] = ('Average Salary', 'Employee Count', 'Average Employment Time')  # Add all your report types here
report_type_dropdown.grid(row=0, column=0)

# poga reporta ģenerēšanai
generate_button = tk.Button(root, text='Generate Report', command=generate_report)
generate_button.grid(row=1, column=0)

# teksta lauks rezultātiem
output_text = tk.Text(root, wrap='word', height=30, width=80)
output_text.grid(row=2, column=0)

# palaiž GUI
root.mainloop()
