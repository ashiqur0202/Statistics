# Create a box plot for a dataset to visualize its distribution.

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def create_box_plot(df):
    sns.set(style='whitegrid')
    plt.figure(figsize=(8, 6))

    sns.boxplot(x='Category', y='Value', data=df)

    plt.title("Box Plot of the Dataset")
    plt.show()

data = {
    'Category': ['A', 'A', 'B', 'B', 'c', 'c'],
    'Value': [25, 30, 15, 20, 35, 40]
}

df = pd.DataFrame(data)

create_box_plot(df)