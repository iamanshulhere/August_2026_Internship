import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the COVID-19 dataset
df = pd.read_csv("full_grouped.csv")

# Display the first 5 rows
print("First 5 Rows")
print(df.head())

# Display dataset information
print("\nDataset Information")
df.info()

# Check for missing values
print("\nMissing Values")
print(df.isnull().sum())

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Calculate total confirmed cases for each date
daily_cases = df.groupby("Date")["Confirmed"].sum()

print("\nGlobal Cases by Date")
print(daily_cases.head())

# Find the top 5 countries by confirmed cases
top_5_countries = (
    df.groupby("Country/Region")["Confirmed"]
    .max()
    .sort_values(ascending=False)
    .head(5)
)

print("\nTop 5 Countries by Confirmed Cases")
print(top_5_countries)

# Plot Top 5 Countries
plt.figure(figsize=(10, 6))

plt.bar(top_5_countries.index, top_5_countries.values)

plt.title("Top 5 Countries by Confirmed COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Confirmed Cases")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# Select numerical columns for correlation analysis
correlation_data = df[
    ["Confirmed", "Deaths", "Recovered", "Active", "New cases", "New deaths", "New recovered"]
]

# Calculate correlation matrix
correlation_matrix = correlation_data.corr()

# Create heatmap
plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.title("Correlation Heatmap of COVID-19 Variables")
plt.tight_layout()

plt.show()

# Create scatter plot of confirmed cases vs deaths
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Confirmed",
    y="Deaths"
)

plt.title("Confirmed COVID-19 Cases vs Deaths")
plt.xlabel("Confirmed Cases")
plt.ylabel("Deaths")

plt.tight_layout()
plt.show()