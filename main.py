import csv
import numpy as np

# open and read file with delimiter from csv, pop out headers 
with open("titanic1.csv", "r") as file:
    data = csv.reader(file, delimiter=",")
    row_headers = next(data)
    data_rows_as_list = list(data)
    titanic_data1 = np.array(data_rows_as_list)

# open and read file 2 with delimiter from csv, pop out headers 
with open("titanic2.csv", "r") as file:
    data = csv.reader(file, delimiter=",")
    row_headers = next(data)
    data_rows_as_list = list(data)
    titanic_data2 = np.array(data_rows_as_list)

# add, multiple or concatenate arrays together
# print(titanic_data1 * titanic_data2)
# concat arrays together 
combined_data = np.concatenate((titanic_data1, titanic_data2), axis=0)
# find out how many arrays in dataset 
print(combined_data.ndim) 
# find out shape of dataset (length across each dimension e.g. arrays in arrays, columns & row numbers)
print(combined_data.shape)
