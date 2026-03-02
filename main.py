import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 1) 
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
for row in listify:
    titanic_string = (",").join(row)
    titanic_lists_to_string.append(titanic_string)

# write to new file
complete_titanic_list = ("\n").join(titanic_lists_to_string)

with open("titanic.csv", "w") as file:
    # To select the headers and data columns you like to add to the CSV file, you’d write: ('Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare\n'). Writing \n at the end of the headers indicates to Python that the rest of the Titanic data should start on the next row.
          file.write(complete_titanic_list)


with open("titanic.csv", "r") as file:
  data = csv.reader(file, delimiter=",")
  row_headers = next(data)
  data = list(data)
  data = np.array(data)

survived = np.array(data[:, [0]], dtype=int).flatten()

fare = np.array(data[:, [7]], dtype=float).flatten()

fare_survived = []
fare_not_survived = []
for index in range(0, len(fare)):
  if survived[index] == 1:
    fare_survived.append(fare[index])
  else:
    fare_not_survived.append(fare[index])

bins = range(0, 240, 15)

plt.hist(fare_survived, alpha=0.8, histtype="bar", color="green")
plt.hist(fare_not_survived, alpha=0.5, histtype="bar", color="red")

plt.xticks(range(0,240,20))
plt.yticks(range(0,360,25))
plt.xlabel("Fare (£)")
plt.ylabel("Number of passengers")
plt.title("Fare distribution of Titanic passengers")
plt.gca().legend(("Survived", "Not Survived"))

plt.savefig("fare_distribution_titanic.png")
plt.show()

# TITANIC SCATTER PLOT 
dataframe = pd.read_csv("titanic.csv")
dataframe = dataframe.replace({"Survived" : {0: "Did NOT Survive", 1: "Survived"}})
sns.scatterplot(x="Age", y="Fare", hue="Survived", data=dataframe)
plt.xlabel("Passenger Age")
plt.ylabel("Passenger Fare (£)")

plt.savefig("titanic_scatter_plot.png")
plt.show()

# print(
#     f"Average fare of a survived passenger: £{round(np.mean(fare_survived),2)}"
# )
# print(
#     f"The Average fare of the casualties were: £{round(np.mean(fare_not_survived), 2)}"
# )

# print(
#     "Inference - the higher the cost of ticket & therefore class, the higher the survival rate."
# )

# print(
#     f"Median fare of a survived passenger: £{round(np.median(fare_survived),2)}"
# )
# print(
#     f"The median fare of the casualties were: £{round(np.median(fare_not_survived), 2)}"
# )


# data aggregation: find min & max vals, calc the mean, calc the median, calc the sum of all vals, create scatter plot with summarized data
# min value finder 
# print(np.min(combined_data))
# # max value finder 
# print(np.max(combined_data))
# # show min in a string 
# print(f"The minimum value of 'combined data' is: {np.min(combined_data)}")
# # show max in a string 
# print(f"The maximum value of 'combined data' is: {np.max(combined_data)}")
# # find average 
# print(f"The average time of 'combined data' is: {np.mean(combined_data)}")
# # find median
# print(f"The median of 'combined data' is: {np.median(combined_data)}")
# # find sum of all vals
# print(f"The sum of all values in 'combined data' is: {np.sum(combined_data)}")

# # 2)  
# # creating scatter plot 
# plt.scatter(combined_data, age)
# plt.xlabel("Number of passengers")
# plt.ylabel("Number of survivors")
# plt.title("Scatter Chart of Titanic Survivors")
# plt.savefig("scatter_plot_titanic.png")
# plt.show()

