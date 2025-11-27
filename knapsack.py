def knapsack_01_greedy(weights, values, capacity):
    items = sorted([(v / w, w, v) for w, v in zip(weights, values)], reverse=True)
    total_value = 0
    chosen_items = []

    for ratio, weight, value in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
            chosen_items.append((weight, value))
    return total_value, chosen_items

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print(knapsack_01_greedy(weights, values, capacity))
