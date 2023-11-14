# Implement a function to generate a probability distribution for a given set of events.

def calculate_probability_distribution(events):
    total_occurrences = sum(events.values())
    probability_distribution = {event: occurrences / total_occurrences for event, occurrences in events.items()}
    return probability_distribution

event = {'A': 10, 'B':5, 'C': 8, 'D': 12}

result = calculate_probability_distribution(event)

print("Probability Distribution:")

for event, probability in result.items():
    print(f"{event}: {probability:.2f}")