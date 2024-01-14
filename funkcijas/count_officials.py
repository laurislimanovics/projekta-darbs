import pandas as pd

def count_officials(dataframe, column_name='Amatpersona'):
    counts = dataframe[column_name].value_counts()
    
    officials_count = {
        'amatpersonas': counts.get(True, 0),  # Pārbauda, vai True eksistē, ja ne, atgriež 0
        'nav amatpersonas': counts.get  (False, 0)  # Pārbauda, vai False eksistē, ja ne, atgriež 0
    }
    return officials_count