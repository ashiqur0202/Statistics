# Write a function that takes a list of strings and returns a list of the unique strings in the list.

import pandas as pd

def unique_string(list_of_string):
    df = pd.Series(list_of_string)
    unique = df.unique()
    return unique.tolist()

list_of_string = ["hi", 'hello', 'hru?', 'hi']

result = unique_string(list_of_string)

print(result)