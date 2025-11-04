---
title: Pandas
parent: Packages
---

# Read Data
- all data on pandas are basically of two types
- dataframe (2d data/table), series (1d data/list)

### Read data from csv file
```python
import pandas

# load data from csv file to data frame
df: pandas.DataFrame
df = pandas.read_csv("weather_data.csv")

# print entire table
print(df)

# print only temp column
temperatureSeries: pandas.Series
temperatureSeries = df["temp"]

# use of data frame with functions
print("Temperature Summary")
print(f"Min Temp:{temperatureSeries.min()}")
print(f"Max Temp:{temperatureSeries.max()}")
print(f"Mean Temp:{temperatureSeries.mean()}")
```

# Write Data

### create new csv file from data
```python
import pandas

data_dict = {"students": ["Vivek", "Deven", "Druv"], "Scores": [50, 60, 70]}

# Create new data from out of dict
data: pandas.DataFrame
data = pandas.DataFrame(data_dict)

# print data
print(data)

# print to new filr
data.to_csv("TestScore.csv")
```
