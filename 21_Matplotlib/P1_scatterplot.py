"""Demonstrates creation of a scatter plot using Matplotlib."""

import matplotlib.pyplot as plt
import numpy as np

#1. First Dataset ---

# x_data_1: Represents the independent variable (e.g., hours studied)
x_data_1 = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
# y_data_1: Represents the dependent variable (e.g., test score)
y_data_1 = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

# plt.scatter() creates a scatter plot. The 'label' is used for the legend.
plt.scatter(x_data_1, y_data_1, label="Group A Scores", color='blue', alpha=0.7)


#2. Second Dataset ---

x_data_2 = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
y_data_2 = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])

# This call adds a second set of points to the SAME figure.
plt.scatter(x_data_2, y_data_2, label="Group B Scores", color='red', alpha=0.7, marker='x')


#3. Customizing the Visualization (Best Practice) ---

plt.title("Comparison of Two Data Groups") # Title of the plot
plt.xlabel("Independent Variable (X)")     # Label for the x-axis
plt.ylabel("Dependent Variable (Y)")     # Label for the y-axis
plt.legend()                              # Shows the labels defined in the scatter calls
plt.grid(True, linestyle='--', alpha=0.6) # Add a grid for readability

# plt.show() displays the compiled plot window.
plt.show()