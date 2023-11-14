# Write a function to calculate the mean and median of a list of numbers.

def calculate_mean_median(numbers):
    mean = sum(numbers)/len(numbers) 
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]
    
    return mean, median

number_list = [1, 2, 3, 6, 7, 9, 10, 15, 17, 60, 90, 99]

mean_result, median_result = calculate_mean_median(number_list)

print("Mean is: ", mean_result)
print("Median is: ", median_result)

