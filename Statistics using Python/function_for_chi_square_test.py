# Conduct a chi-square test for independence on a contingency table.

import numpy as np
from scipy.stats import chi2_contingency

def chi_square_test(data):
    chi2, p, dof, expected = chi2_contingency(data)

    print("Chi-Square Statistic:", chi2)
    print("P-value:", p)
    print("Degrees of Freedom:", dof)
    print("Expected Frequencies:")
    print(expected)

contingency_table = np.array([[20, 10], [20, 40]])

chi_square_test(contingency_table)