# Plot a histogram of a given dataset using Matplotlib or Seaborn.

import matplotlib.pyplot as plt
import numpy as np

def plot_histogram(data, bins=10):
    plt.hist(data, bins=bins, edgecolor='black')
    plt.title('Histogram of the Dataset')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.show()

dataset = np.random.randn(1000)

plot_histogram(dataset)