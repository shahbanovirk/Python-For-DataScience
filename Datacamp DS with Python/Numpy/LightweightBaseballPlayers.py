# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
# height and weight are available as a regular lists

# Import numpy
import numpy as np
height_in = [75.75,76,77,78,80,90,74,73,76]

weight_lb = [160.180,165,180,170,172,180,173,165,165]
# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi<21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[bmi<21])