import pandas as pd
import numpy as np

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphone", "Computer"],
    "Quantity": [10, np.nan, 5, 8, np.nan],
    "Price": [1500, 800, np.nan, 200, 3000]
}

df = pd.DataFrame(data)
df.fillna(df.mean(numeric_only=True), inplace=True)

print ("Dataset after filling missing values:")
print(df)
