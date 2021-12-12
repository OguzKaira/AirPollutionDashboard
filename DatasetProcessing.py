# Dataset Processing
import pandas as pd

# Read CSV File
data = pd.read_csv("death-rates-from-air-pollution.csv")

# Getting Column from Dataset
data = data.iloc[:, 0:4]

# Delete Irevelent Column
data = data.drop(["Code"] , axis = 1)

# Delete NA Rows
data = data.dropna()

# Change Column Names
data = data.rename({"Entity": "Country", "Year": "Year", "Air pollution (total) (deaths per 100,000)": "Deaths"}, axis=1)

# Splitting only rows containing 2017 data
data = data[data.Year == 2017]

# Download New Dataset
data.to_csv("PollutionDataset.csv")
