"""Demonstrates usage of subplots to display multiple graphs using Matplotlib."""

import matplotlib.pyplot as plt 
import numpy as np

# Define the common x-axis data
x_data = np.array([0, 1, 2, 3])

# Define the two alternating datasets
data_set_1 = np.array([3, 8, 1, 10])
data_set_2 = np.array([10, 20, 30, 40])

# Define the figure size for better viewing
plt.figure(figsize=(12, 6))
# Set a master title for the entire figure
plt.suptitle("Six Subplots in a 2x3 Grid", fontsize=16)

# The loop iterates 6 times (for plots 1 through 6)
for i in range(1, 7):
    # Select the subplot location: 2 rows, 3 columns, position i
    plt.subplot(2, 3, i)
    
    # Check the plot number to alternate the dataset
    if i % 2 != 0: # Odd numbered plots (1, 3, 5)
        plt.plot(x_data, data_set_1, marker='o', color='darkorange')
        plt.title(f"Plot {i} (Dataset 1)")
        
    else: # Even numbered plots (2, 4, 6)
        plt.plot(x_data, data_set_2, marker='x', color='darkcyan')
        plt.title(f"Plot {i} (Dataset 2)")
        
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.grid(True, linestyle=':', alpha=0.6)

# Adjust the spacing between subplots to prevent overlap
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show the final compiled figure
plt.show()