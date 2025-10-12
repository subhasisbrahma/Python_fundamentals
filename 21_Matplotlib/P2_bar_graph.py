"""Demonstrates creation of a bar graph using Matplotlib."""

import matplotlib.pyplot as plt 
import numpy as np

# Define categories (X-axis labels)
categories = np.array(["A", "B", "C", "D"]) 
# Define values (Y-axis heights)
values = np.array([3, 8, 1, 10])

# Create the Vertical Bar Chart
# plt.bar(x, y) plots the categories against their corresponding values.
plt.bar(categories, values, color='teal') 


# Set the title and axis labels for clarity
plt.title("Comparison of Category Values") 
plt.xlabel("Category")
plt.ylabel("Value") 
plt.grid(axis='y', linestyle='--', alpha=0.7) # Add a horizontal grid for easy reading

# If you prefer a horizontal bar chart:
# plt.barh(categories, values, color='skyblue')

# plt.show() displays the final plot window.
plt.show()