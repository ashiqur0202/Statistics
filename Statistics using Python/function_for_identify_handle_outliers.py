# Identify and handle outliers in a dataset using statistical methods.

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def handle_outliers(data):
    z_scores = np.abs(stats.zscore(data))

    threshold = 3

    outliers = np.where(z_scores > threshold)[0]

    data_no_outliers = np.copy(data)
    for idx in outliers:
        data_no_outliers[idx] = np.median(data)

    return data_no_outliers

np.random.seed(42)
data_with_outliers = np.random.normal(0, 1, 1000)
data_with_outliers[50] = 10 

data_no_outliers = handle_outliers(data_with_outliers)

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.title('Original Data with Outlier')
plt.hist(data_with_outliers, bins=50, color='blue', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.subplot(2, 1, 2)
plt.title('Data after Outlier Handling')
plt.hist(data_no_outliers, bins=50, color='green', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
