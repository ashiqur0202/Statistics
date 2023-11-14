# Apply bootstrapping or permutation tests to assess the stability of results.

import numpy as np

def perform_bootstrapping(data, num_samples=1000, statistic=np.mean):
    n = len(data)
    bootstrap_samples = np.empty(num_samples)

    for i in range(num_samples):
        bootstrap_sample = np.random.choice(data, size=n, replace=True)
        bootstrap_statistic = statistic(bootstrap_sample)
        bootstrap_samples[i] = bootstrap_statistic

    return bootstrap_samples

original_data = np.random.normal(loc=10, scale=2, size=1000)

bootstrap_means = perform_bootstrapping(original_data)

print("Original Mean:", np.mean(original_data))
print("Bootstrap Mean (95% CI):", np.percentile(bootstrap_means, [2.5, 97.5]))