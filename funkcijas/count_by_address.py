def count_employees_by_address(dataframe):
    address_counts = dataframe['Darba vietas adrese'].value_counts()
    return address_counts
