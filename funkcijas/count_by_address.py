def count_employees_by_address(dataframe):
    address_counts = dataframe['Darba vietas adrese'].value_counts().to_dict()
    return address_counts
