"""Demonstrates creation of a histogram using Matplotlib."""

import matplotlib.pyplot as plt 
import numpy as np

# 1. Data Generation (Using a Normal/Gaussian Distribution)
# np.random.normal(loc, scale, size) generates random numbers:
#   loc=170 (Mean/Center of the data, analogous to height in cm)
#   scale=10 (Standard deviation/Spread of the data)
#   size=250 (Number of data points)
data_points = np.random.normal(170, 10, 250)

# 2. Create the Histogram
# plt.hist(x) plots the distribution. It automatically groups the data into bins 
# (frequency intervals) and displays the count (frequency) of values in each bin.
plt.hist(data_points, bins=20, color='skyblue', edgecolor='black', alpha=0.7) 
# Note: 'bins=20' explicitly sets the number of intervals, improving clarity.


plt.title("Distribution of Sample Data (Normal Distribution)") 
plt.xlabel("Value Range (Bins)")
plt.ylabel("Frequency (Count)")
plt.grid(axis='y', linestyle='--', alpha=0.6) # Add a horizontal grid
plt.axvline(np.mean(data_points), color='red', linestyle='dashed', linewidth=1, label=f'Mean: {np.mean(data_points):.2f}')
plt.legend()

# plt.show() displays the final plot window.
plt.show()