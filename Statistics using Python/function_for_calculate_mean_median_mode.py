# Write a function that takes a list of numbers and calculates the mean, median, and mode.

import pandas as pd
import numpy as np

def calculate_mean_median_mode(list_of_numbers):
    
  series = pd.Series(list_of_numbers)

  mean = series.mean()
  median = series.median()
  mode = series.mode()

  return mean, median, mode


list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mean, median, mode = calculate_mean_median_mode(list_of_numbers)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
