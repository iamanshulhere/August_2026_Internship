import pandas as pd

# Load the Mathematics student dataset
df = pd.read_csv("Maths.csv", sep=";", encoding="latin1")

# Display first five rows
print("First 5 Rows")
print(df.head())

# Display dataset shape
print("\nDataset Shape")
print(df.shape)

# Display column names
print("\nColumn Names")
print(df.columns.tolist())

# Check missing values
print("\nMissing Values")
print(df.isnull().sum())