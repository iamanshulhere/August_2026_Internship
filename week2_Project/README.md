# Week 2 Project - COVID-19 Data Visualization

## Internship

BeeSkilled - Data Science with Python Internship

## Objective

The objective of this project is to learn and practice data visualization
using Python, Pandas, Matplotlib, and Seaborn.

The project analyzes COVID-19 data and presents important patterns and
relationships through different types of visualizations.

---

## Dataset

**Dataset Name:** full_grouped.csv

The dataset contains COVID-19 information for different countries and dates.

Important columns used in this project include:

- `Date` - Date of the COVID-19 record
- `Country/Region` - Country or region name
- `Confirmed` - Confirmed COVID-19 cases
- `Deaths` - COVID-19 deaths
- `Recovered` - Recovered cases
- `Active` - Active cases
- `New cases` - Newly reported cases
- `New deaths` - Newly reported deaths
- `New recovered` - Newly reported recoveries
- `WHO Region` - WHO region

---

## Project Tasks

The following data visualization tasks were performed:

1. Load the COVID-19 dataset using Pandas.
2. Check the dataset structure and missing values.
3. Convert the Date column into datetime format.
4. Analyze the trend of confirmed COVID-19 cases over time.
5. Identify and compare the top 5 countries based on confirmed cases.
6. Create a correlation heatmap for numerical COVID-19 variables.
7. Create a scatter plot showing the relationship between confirmed cases and deaths.

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

---

## Visualizations

### 1. COVID-19 Cases Trend

A line chart is used to visualize the change in confirmed COVID-19 cases
over time.

The `Date` column is converted to datetime format and confirmed cases are
grouped by date.

### 2. Top 5 Countries

A bar chart is used to compare the five countries with the highest recorded
confirmed COVID-19 cases.

### 3. Correlation Heatmap

A Seaborn heatmap is used to visualize correlations between numerical
COVID-19 variables such as:

- Confirmed
- Deaths
- Recovered
- Active
- New cases
- New deaths
- New recovered

Correlation values range from -1 to +1.

### 4. Confirmed Cases vs Deaths

A scatter plot is used to visualize the relationship between confirmed
COVID-19 cases and deaths.

---

## Project Structure

```text
week2_Project/
│
├── screenshots/
│   ├── 01_dataset_loaded.png
│   ├── 02_missing_values.png
│   ├── 03_cases_trend.png
│   ├── 04_top_5_countries.png
│   ├── 05_correlation_heatmap.png
│   └── 06_cases_vs_deaths_scatter.png
│
├── covid_analysis.py
├── full_grouped.csv
└── README.md