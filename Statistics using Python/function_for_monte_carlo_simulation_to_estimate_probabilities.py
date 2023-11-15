# Use Monte Carlo simulation to estimate probabilities

import random

def monte_carlo_simulation(num_trials):
    heads_count = 0

    for _ in range(num_trials):
        outcome = random.choice([0, 1])
        heads_count += outcome

    probability_heads = heads_count / num_trials
    
    return probability_heads

num_trials = 100000
    
estimated_probability = monte_carlo_simulation(num_trials)

print(f"Estimated Probability of Heads: {estimated_probability}")