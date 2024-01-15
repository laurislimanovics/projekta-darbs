import pandas as pd

def count_education_levels(file_path):
    df = pd.read_excel(file_path)

    # aizpilda tukšās vērtības ar "Nav augstākās izglītības"
    df['Grāda veids'] = df['Grāda veids'].fillna('Nav augstākās izglītības')

    # noņem dublikātus
    df = df.drop_duplicates(subset=['Darbinieka kods'])

    # aprēķina un atgriež rezultātus
    education_counts = df['Grāda veids'].value_counts()
    return education_counts
