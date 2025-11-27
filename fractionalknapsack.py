# Fractional Knapsack (Greedy Optimal)

def fractional_knapsack(weights, values, capacity):
    items = sorted([(v / w, w, v) for w, v in zip(weights, values)], reverse=True)
    total_value = 0.0
    chosen_items = []
    for ratio, weight, value in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
            chosen_items.append((weight, value))
        else:
            total_value += ratio * capacity
            chosen_items.append((capacity, ratio * capacity))
            break
    return total_value, chosen_items


# Example
weights = [10, 40, 20, 30]
values = [60, 40, 100, 120]
capacity = 50
val, items = fractional_knapsack(weights, values, capacity)
print("Max Value:", val)
print("Items taken (weight, value):", items)
