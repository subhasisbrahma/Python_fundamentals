"""Demonstrates creation of a pie chart using Matplotlib."""

import matplotlib.pyplot as plt
import numpy as np

# 1. Define the data (proportional values)
proportions = np.array([35, 25, 25, 15]) 
# 2. Define the labels for each slice
slice_labels = ["Apples", "Bananas", "Cherries", "Dates"]

# 3. Customizing the chart
# explode: An array to specify how far each wedge should be driven from the center.
# We'll highlight the "Apples" slice.
explode_slices = [0.1, 0, 0, 0]

# colors: Define a color scheme
colors = ['lightcoral', 'gold', 'lightskyblue', 'lightgreen']

# plt.pie() creates the chart
plt.pie(
    proportions,
    labels=slice_labels,
    startangle=90,          # Start the first slice at the top (90 degrees)
    explode=explode_slices, # Apply the explosion array
    colors=colors,          # Apply the color array
    autopct='%1.1f%%',      # Automatically format and display the percentage on the slices (one decimal place)
    shadow=True             # Add a slight shadow for visual effect
)

# Add a title and ensure the chart is displayed as a circle (equal aspect ratio)
plt.title("Fruit Sales Distribution")
plt.axis('equal') 

# plt.show() displays the final plot window.
plt.show()