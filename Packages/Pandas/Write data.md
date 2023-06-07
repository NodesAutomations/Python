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
