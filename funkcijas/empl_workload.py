def count_employees_by_workload(dataframe):
    workload_counts = dataframe['Slodze'].value_counts()
    return workload_counts
