import pandas as pd

def check_if_on_vacation(dataframe, replacement_column='Aizvietotājs'):
    # Pārbauda, vai kolonnā 'Aizvietotājs' ir ierakstīts teksts
    is_on_vacation = dataframe[replacement_column].apply(lambda x: not pd.isna(x) and x != '')
    
    # Atgriež rezultātu kā DataFrame kolonnu
    return is_on_vacation