import sys
import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Funkcijas importēšana no funkciju failiem
from funkcijas.avg_salary import average_salary
from funkcijas.count_employees import count_employees_per_division
# Ielādē datus no Excel faila
df = pd.read_excel('empl.xlsx')
education_file_path = 'education.xlsx'

# Nodaļu saraksts
division_list = ['Jelgavas reģionālā nodaļa', 'Daugavpils reģionālā nodaļa', 'Valmieras reģionālā nodaļa', 'Ventspils reģionālā nodaļa', 'Liepājas reģionālā nodaļa', 
                 'Rēzeknes reģionālā nodaļa', 'Rīgas pilsētas Zemgales nodaļa', 'Rīgas pilsētas Latgales nodaļa', 'Pārvaldes struktūrvienības', 'Starptautisko pakalpojumu nodaļa', 
                 'Informācijas apstrādes nodaļa', 'Iemaksu nodaļa', 'Slepenības režīma nodrošināšanas nodaļa']

def generate_pie_chart():
    # Saņem izvēlēto ziņojuma veidu no nolaižamā saraksta
    report_type = report_type_var.get()
    if report_type == 'Nodaļu vidējās algas':
        result = average_salary(division_list, df)
        
        # Ģenerē tortes diagrammu, pamatojoties uz rezultātu ar vidējo algu
        plt.figure(figsize=(8, 8)) 
        plt.pie(result.values(), labels=result.keys(), autopct=lambda p: f'€{p*sum(result.values())/100:.2f}' if p > 2 else '', textprops={'fontsize': 10})
        plt.title("Nodaļu vidējās algas")
        plt.show()
    elif report_type == 'Darbinieku skaits nodaļās':
        result = count_employees_per_division(division_list, df)

        # Ģenerē tortes diagrammu, pamatojoties uz rezultātu ar vidējo algu
        plt.figure(figsize=(8, 8)) 
        plt.pie(result.values(), labels=result.keys(), autopct=lambda p: f'{int(p * sum(result.values()) / 100)}', textprops={'fontsize': 10})
        plt.title("Darbinieku skaits nodaļās")
        plt.show()
# Funkcija tabulas ziņojuma ģenerēšanai
def generate_table_report():
    # Saņem izvēlēto ziņojuma veidu no nolaižamā saraksta
    report_type = report_type_var.get()
    if report_type == 'Nodaļu vidējās algas':
        result = average_salary(division_list, df)
        
        # Izveido jaunu logu tabulas rādīšanai
        table_window = tk.Toplevel(root)
        table_window.title('Tabulas ziņojums')
        
        # Izveido Treeview logrīka izveidošanai
        tree = ttk.Treeview(table_window, columns=("Nodaļa", "Vidējā alga"), show="headings")
        tree.heading("Nodaļa", text="Nodaļa", anchor="center")  
        tree.heading("Vidējā alga", text="Vidējā alga", anchor="center")  
        tree.column("Nodaļa", width=300)  
        tree.column("Vidējā alga", width=150)

        # Izveido vertikālu ritjoslu
        tree_scrollbar = ttk.Scrollbar(table_window, orient="vertical", command=tree.yview)
        tree.configure(yscroll=tree_scrollbar.set)

        # Iepakojiet Treeview un ritjoslu
        tree.grid(row=0, column=0, sticky="nsew")
        tree_scrollbar.grid(row=0, column=1, sticky="ns")

        # Ievietojiet datus Treeview logrīkā ar centrētu izlīdzinājumu
        for division, avg_salary in result.items():
            tree.insert("", "end", values=(division, f"{avg_salary:.2f} EUR"))

        # Pievieno režģus Treeview
        style = ttk.Style()
        style.configure("Treeview", rowheight=25, font=('Helvetica', 10))
        tree.tag_configure("centered", anchor="center")

        # Konfigurējiet režģus
        table_window.grid_rowconfigure(0, weight=1)
        table_window.grid_columnconfigure(0, weight=1)
    elif report_type == 'Darbinieku skaits nodaļās': 
        employee_counts = count_employees_per_division(division_list, df)

        # Izveido jaunu logu tabulas rādīšanai
        table_window = tk.Toplevel(root)
        table_window.title('Tabulas ziņojums')

        # Izveido Treeview logrīka izveidošanai
        tree = ttk.Treeview(table_window, columns=("Nodaļa", "Darbinieku skaits"), show="headings")
        tree.heading("Nodaļa", text="Nodaļa", anchor="center")  
        tree.heading("Darbinieku skaits", text="Darbinieku skaits", anchor="center")  
        tree.column("Nodaļa", width=300)  
        tree.column("Darbinieku skaits", width=150)

        # Izveido vertikālu ritjoslu
        tree_scrollbar = ttk.Scrollbar(table_window, orient="vertical", command=tree.yview)
        tree.configure(yscroll=tree_scrollbar.set)

        # Iepakojiet Treeview un ritjoslu
        tree.grid(row=0, column=0, sticky="nsew")
        tree_scrollbar.grid(row=0, column=1, sticky="ns")

        # Ievietojiet datus Treeview logrīkā ar centrētu izlīdzinājumu
        for division, employee_count in employee_counts.items():
            tree.insert("", "end", values=(division, f"{employee_count}"))

        # Pievieno režģus Treeview
        style = ttk.Style()
        style.configure("Treeview", rowheight=25, font=('Helvetica', 10))
        tree.tag_configure("centered", anchor="center")

        # Konfigurējiet režģus
        table_window.grid_rowconfigure(0, weight=1)
        table_window.grid_columnconfigure(0, weight=1)
def generate_bar_chart():
    # Saņem izvēlēto ziņojuma veidu no nolaižamā saraksta
    report_type = report_type_var.get()
    if report_type == 'Nodaļu vidējās algas':
        result = average_salary(division_list, df)
        
        # Pārvērst vārdnīcas atslēgas sarakstu
        divisions = list(result.keys())
        
        # Ģenerē horizontālu joslu diagrammu ar nodaļām un vidējām algām
        plt.figure(figsize=(8, 6))
        bars = plt.barh(divisions, result.values(), color='royalblue')
        plt.xlabel('Vidējā alga (EUR)')
        plt.title('Nodaļu vidējās algas')
        
        # Anotē joslas ar faktiskajām algu vērtībām uz virsotnēm
        for bar, salary in zip(bars, result.values()):
            plt.text(salary - 250, bar.get_y() + bar.get_height() / 2, f'{salary:.2f} EUR', ha='center', va='center', fontsize=10)
        
        plt.tight_layout()
        plt.show()
    elif report_type == 'Darbinieku skaits nodaļās': 
        employee_counts = count_employees_per_division(division_list, df)

        # Pārvērst vārdnīcas atslēgas sarakstu
        divisions = list(employee_counts.keys())

        # Ģenerē horizontālu joslu diagrammu ar nodaļām un darbinieku skaitu
        plt.figure(figsize=(8, 6))
        bars = plt.barh(divisions, employee_counts.values(), color='royalblue')
        plt.xlabel('Darbinieku skaits')
        plt.title('Darbinieku skaits nodaļās')

        # Anotē joslas ar faktiskajiem darbinieku skaita vērtībām uz virsotnēm
        for bar, count in zip(bars, employee_counts.values()):
            plt.text(count + 5, bar.get_y() + bar.get_height() / 2, f'{count}', ha='center', va='center', fontsize=10)

        plt.tight_layout()
        plt.show()
# Izveido galveno Tkinter logu
root = tk.Tk()
root.title('Ziņojumu ģenerators')
root.geometry('250x250')  # Iestatiet loga izmēru uz 250x250

# Ziņojuma veida izvēles teksts
report_label = tk.Label(root, text="Izvēlieties ziņojumu", font=('Helvetica', 10))
report_label.pack(pady=5)

# Dropdown saraksts, lai izvēlētos ziņojuma veidu
report_type_var = tk.StringVar()
report_type_dropdown = ttk.Combobox(root, textvariable=report_type_var)
report_type_dropdown['values'] = ('Nodaļu vidējās algas', 'Darbinieku skaits', 'Vidējais nodarbinātības laiks')  # Ziņojumu veidu saraksts
report_type_dropdown.pack(pady=5)

# Poga ziņojuma ģenerēšanai kā tortes diagrammu
generate_pie_chart_button = tk.Button(root, text='Ģenerēt tortes diagrammu', command=generate_pie_chart)
generate_pie_chart_button.pack(pady=5)

# Poga ziņojuma ģenerēšanai kā tabulu
generate_table_report_button = tk.Button(root, text='Ģenerēt tabulu', command=generate_table_report)
generate_table_report_button.pack(pady=5)

# Poga ziņojuma ģenerēšanai kā joslu diagrammu
generate_bar_chart_button = tk.Button(root, text='Ģenerēt joslu diagrammu', command=generate_bar_chart)
generate_bar_chart_button.pack(pady=5)

def on_closing():
    root.destroy()  # Iznīcināt galveno logu
    plt.close('all')  # Aizver visus Matplotlib logus
    sys.exit(0)  # Iziet no programmas

# Pievieno funkciju, kas tiek izsaukta, kad tiek aizvērts galvenais logs
root.protocol("WM_DELETE_WINDOW", on_closing)

# Sāk Tkinter logu
root.mainloop()
