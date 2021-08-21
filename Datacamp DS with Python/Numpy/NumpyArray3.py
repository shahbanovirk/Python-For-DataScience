# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# height and weight are available as regular lists

# Import numpy
import numpy as np
height_in =[172,173,175,178,173,175,172,170,179,178,180,190]
weight_lb = [70,95,77,78,80,82,90,86,74,73,70.70,72]
# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
weight = np.array(weight_lb)

np_weight_kg = weight * 0.453592

# Calculate the BMI: bmi
BMI = np_weight_kg / np_height_m **2

# Print out bmi
print (BMI)