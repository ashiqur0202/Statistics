# Set up and analyze results from an A/B test

import numpy as np
import scipy.stats as stats

def ab_test_analysis(group_a, group_b, alpha=0.05):
    t_stat, p_value = stats.ttest_ind(group_a, group_b)

    if p_value < alpha:
        result = "Statistically significant! We reject the null hypothesis."
    else:
        result = "Not statistically significant. We fail to reject the null hypothesis."

    return result, p_value

np.random.seed(42)
group_a = np.random.normal(loc=20, scale=5, size=100)
group_b = np.random.normal(loc=22, scale=5, size=100)

result, p_value = ab_test_analysis(group_a, group_b)

print("A/B Test Result:", result)
print("P-Value:", p_value)