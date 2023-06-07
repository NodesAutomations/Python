### Read data from csv file
```python
import pandas

# load data from csv file to data frame
df = pandas.read_csv("weather_data.csv")

# print entire table
print(df)

# print only temp column
print(df["temp"])
```
