
import pandas as pd

data = {

    "id" :[1,2,3,4,5],
    "name" : ["Alice", "Bob", "Charlie", "David", "Eve"],
    "age" :[25, 30, 35, 40, 45],
    "city" : ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
}

df = pd.DataFrame(data)
print(df)
