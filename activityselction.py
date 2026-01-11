# Activity Selection Problem (Greedy Optimal)

def activity_selection(start, finish):
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    chosen = []
    last_finish = -1
    for s, f in activities:
        if s >= last_finish:
            chosen.append((s, f))
            last_finish = f
    return chosen


# Example

start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
selected = activity_selection(start, finish)
print("Selected Activities (start, finish):", selected)

