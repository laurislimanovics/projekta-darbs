import pandas as pd

def check_if_being_replaced(dataframe, replacement2_column='Aizvieto'):
    # Pārbauda, vai kolonnā 'Aizvietotājs' ir ierakstīts teksts
    is_replaced = dataframe[replacement2_column].apply(lambda x: not pd.isna(x) and x != '')
    
    # Atgriež rezultātu kā DataFrame kolonnu
    return is_replaced