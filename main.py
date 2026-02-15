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

# transform array back into list  
listify = combined_data.tolist()
# turn into string 
titanic_lists_to_string = []
for list in listify:
    titanic_string = (",").join(list)
    titanic_lists_to_string.append(titanic_string)

# write to new file
complete_titanic_list = ("/n").join(titanic_lists_to_string)

with open("titanic.csv", "w") as file:
    # To select the headers and data columns you like to add to the CSV file, you’d write: ('Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare\n'). Writing \n at the end of the headers indicates to Python that the rest of the Titanic data should start on the next row.
          file.write(complete_titanic_list)
          
