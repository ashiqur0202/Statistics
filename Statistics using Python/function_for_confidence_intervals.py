# Compute confidence intervals for a given sample.

import numpy as np
from scipy.stats import t

def confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    std_error = np.std(data, ddof=1) / np.sqrt(n)
    margin_of_error = std_error * t.ppf((1 + confidence) / 2, n - 1)

    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error

    return lower_bound, upper_bound

sample_data = [23, 25, 28, 30, 32, 35, 38, 40, 42, 45]

confidence_level = 0.95
lower, upper = confidence_interval(sample_data, confidence_level)

print(f"Confidence Interval ({int(confidence_level * 100)}%):")
print(f"Lower Bound: {lower}")
print(f"Upper Bound: {upper}")