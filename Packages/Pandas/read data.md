### Overview
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
