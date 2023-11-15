# Implement Bayesian methods for parameter estimation

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

true_prob = 0.6

np.random.seed(42)
data = np.random.choice([0, 1], size=100, p=[1 - true_prob, true_prob])

def bayesian_inference(data, prior_alpha=1, prior_beta=1):
    posterior_alpha = prior_alpha + np.sum(data)
    posterior_beta = prior_beta + len(data) - np.sum(data)

    probabilities = np.linspace(0, 1, 1000)

    prior = stats.beta.pdf(probabilities, prior_alpha, prior_beta)
    likelihood = stats.bernoulli.pmf(np.sum(data), p=probabilities)
    posterior = stats.beta.pdf(probabilities, posterior_alpha, posterior_beta)

    return probabilities, prior, likelihood, posterior

probabilities, prior, likelihood, posterior = bayesian_inference(data)

# Plotting
plt.figure(figsize=(12, 6))

# Prior
plt.subplot(2, 2, 1)
plt.plot(probabilities, prior, label='Prior')
plt.title('Prior Distribution')
plt.xlabel('Probability of Success')
plt.ylabel('Density')
plt.legend()

# Likelihood
plt.subplot(2, 2, 2)
plt.plot(probabilities, likelihood, label='Likelihood')
plt.title('Likelihood Function')
plt.xlabel('Probability of Success')
plt.ylabel('Likelihood')
plt.legend()

# Posterior
plt.subplot(2, 2, 3)
plt.plot(probabilities, posterior, label='Posterior')
plt.title('Posterior Distribution')
plt.xlabel('Probability of Success')
plt.ylabel('Density')
plt.legend()

# Combined Plot
plt.subplot(2, 2, 4)
plt.plot(probabilities, prior, label='Prior', linestyle='--')
plt.plot(probabilities, likelihood, label='Likelihood')
plt.plot(probabilities, posterior, label='Posterior')
plt.title('Combined Plot')
plt.xlabel('Probability of Success')
plt.ylabel('Density')
plt.legend()

plt.tight_layout()
plt.show()