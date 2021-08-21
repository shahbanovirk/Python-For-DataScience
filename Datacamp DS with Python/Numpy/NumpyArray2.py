# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# height is available as a regular list

# Import numpy
import numpy as np
height_in = [75.75,76,77,78,80,90,74,73,76]
# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print (np_height_m )