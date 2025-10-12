"""Demonstrates data manipulation and analysis using the Pandas library."""

import pandas as pd

# Define a constant for the file path
FILE_PATH = r"D:\PYTHON_FUNDAMENTALS\20_Pandas\scores.csv" 

# Read the CSV file into a Pandas DataFrame object.
# Pandas is crucial for handling tabular data efficiently.
scores_df = pd.read_csv(FILE_PATH)

# --- 1. Initial Data Inspection ---

print("--- Data Inspection ---")
# Print the entire DataFrame (shows the first/last few rows)
print(scores_df)

# .shape: Returns a tuple representing the dimensions (rows, columns).
print("Shape (Rows, Columns):", scores_df.shape)

# .count(): Returns the number of non-null (non-missing) values for each column.
print("Non-Null Counts per Column:")
print(scores_df.count())

# --- 2. Descriptive Statistics on the 'Total' Column ---

# Select the 'Total' Series and apply aggregation functions:

# .max(): Finds the highest value in the series.
print("Maximum Total Score:", scores_df["Total"].max())

# .min(): Finds the lowest value in the series.
print("Minimum Total Score:", scores_df["Total"].min())

# .mean(): Calculates the arithmetic average of the series.
print("Mean (Average) Total Score:", scores_df["Total"].mean())

# .sum(): Calculates the sum of all values in the series.
print("Sum of All Total Scores:", scores_df["Total"].sum())

# --- 3. Sorting ---

# .sort_values(): Returns a new series sorted in ascending order (default).
print("Total Scores Sorted Ascending:")
print(scores_df["Total"].sort_values())

# .sort_values(ascending=False): Returns a new series sorted in descending order.
print("Total Scores Sorted Descending:")
print(scores_df["Total"].sort_values(ascending=False))