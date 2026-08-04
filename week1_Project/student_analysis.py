import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Info")

print("\nDataset Information")
df.info()

print("\nMissing Values")
print(df.isnull().sum())

print("\nMath Score")
print("Average :", df["math score"].mean())
print("Maximum :", df["math score"].max())
print("Minimum :", df["math score"].min())

print("\nReading Score")
print("Average :", df["reading score"].mean())
print("Maximum :", df["reading score"].max())
print("Minimum :", df["reading score"].min())

print("\nWriting Score")
print("Average :", df["writing score"].mean())
print("Maximum :", df["writing score"].max())
print("Minimum :", df["writing score"].min())

summary = pd.DataFrame({
    "Average": [
        df["math score"].mean(),
        df["reading score"].mean(),
        df["writing score"].mean()
    ],
    "Maximum": [
        df["math score"].max(),
        df["reading score"].max(),
        df["writing score"].max()
    ],
    "Minimum": [
        df["math score"].min(),
        df["reading score"].min(),
        df["writing score"].min()
    ]
},
index=["Math", "Reading", "Writing"])

print("\nSummary Table")
print(summary)