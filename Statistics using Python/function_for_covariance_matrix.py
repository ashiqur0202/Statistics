# Calculate the covariance matrix for a given dataset.

import numpy as np

def calculate_covariance_matrix(dataset):
    if not dataset:
        raise ValueError("Dataset is empty.")

    dataset = np.array(dataset)
    cov_matrix = np.cov(dataset, rowvar=False)

    return cov_matrix

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

covariance_matrix = calculate_covariance_matrix(data)

print("Covariance Matrix:")
print(covariance_matrix)
