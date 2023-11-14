# Implement a function to find the mode of a list of numbers.

def calculate_mode(numbers):

    count_dict = {}
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    max_count = max(count_dict.values())
    mode_list = [key for key, value in count_dict.items() if value == max_count]

    if len(mode_list) == len(numbers):
        return None
    else:
        return mode_list

numbers = [1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 5, 5, 6, 6]
mode_result = calculate_mode(numbers)

print("Mode:", mode_result)
