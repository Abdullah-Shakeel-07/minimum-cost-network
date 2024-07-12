from collections import deque
from queue import PriorityQueue

# Read data from file
def read_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    data_in_file = [line.strip().split(",") for line in lines]
    return data_in_file

# Build dictionary from file data
def build_dictionary(data_in_file):
    dictionary = {}
    for entry in data_in_file:
        key = int(entry[0])
        values = [entry[1:]]
        if key in dictionary:
            dictionary[key].extend(values)
        else:
            dictionary[key] = values
    
    # Preprocess dictionary
    for key, values in dictionary.items():
        for value in values:
            if value[0] == '{}':
                value[0] = key
            value[-1] = float(value[-1])
            if len(value) > 2:
                value[0] = int(value[0][1:])
                del value[1:-1]
            if isinstance(value[0], str):
                value[0] = int(value[0][1:-1])
    return dictionary

# Calculate the cost of a given order
def calculate_cost(order, dictionary):
    total_cost = 0
    for i in range(len(order)):
        matching_list = order[:i+1]
        temp = dictionary[order[i]]
        min_cost = float('inf')
        for parent, cost in temp:
            if parent in matching_list:
                min_cost = min(min_cost, cost)
        total_cost += min_cost
    return total_cost

# Generate all permutations of a list
def permute(order_list):
    if len(order_list) == 0:
        return []
    elif len(order_list) == 1:
        return [order_list]
    else:
        permutations = []
        for i in range(len(order_list)):
            temp = order_list[i]
            remaining_list = order_list[:i] + order_list[i+1:]
            for p in permute(remaining_list):
                permutations.append([temp] + p)
        return permutations

# Depth First Search (DFS) Algorithm
def dfs(initial_order, dictionary):
    stack = deque([initial_order])
    visited = [initial_order]
    initial_cost = calculate_cost(initial_order, dictionary)
    best_order = initial_order

    while stack:
        current_order = stack.pop()
        print(f'Popped: {current_order}, Cost: {calculate_cost(current_order, dictionary)}')
        permutations = permute(current_order)
        for order in permutations:
            cost = calculate_cost(order, dictionary)
            if order not in visited and cost < initial_cost:
                stack.append(order)
                visited.append(order)
                initial_cost = cost
                best_order = order
    
    print(f"\nSolution found using DFS! Order: {best_order}, Cost: {initial_cost}")

# Breadth First Search (BFS) Algorithm
def bfs(initial_order, dictionary):
    queue = [initial_order]
    visited = [initial_order]
    initial_cost = calculate_cost(initial_order, dictionary)
    best_order = initial_order

    while queue:
        current_order = queue.pop(0)
        print(f'Popped: {current_order}, Cost: {calculate_cost(current_order, dictionary)}')
        permutations = permute(current_order)
        for order in permutations:
            cost = calculate_cost(order, dictionary)
            if order not in visited and cost < initial_cost:
                queue.append(order)
                visited.append(order)
                initial_cost = cost
                best_order = order
    
    print(f"\nSolution found using BFS! Order: {best_order}, Cost: {initial_cost}")

# Uniform Cost Search (UCS) Algorithm
def ucs(initial_order, dictionary):
    pq = PriorityQueue()
    visited = [initial_order]
    initial_cost = calculate_cost(initial_order, dictionary)
    pq.put((initial_cost, initial_order))
    best_order = initial_order

    while not pq.empty():
        current_cost, current_order = pq.get()
        print(f'Popped: {current_order}, Cost: {calculate_cost(current_order, dictionary)}')
        permutations = permute(current_order)
        for order in permutations:
            cost = calculate_cost(order, dictionary)
            if order not in visited and cost < initial_cost:
                visited.append(order)
                pq.put((cost, order))
                initial_cost = cost
                best_order = order
    
    print(f"\nSolution found using UCS! Order: {best_order}, Cost: {initial_cost}")

# Main Execution
data_in_file = read_file("data0.txt")
dictionary = build_dictionary(data_in_file)
initial_order = [1, 2, 3, 4, 5]

dfs(initial_order, dictionary)
bfs(initial_order, dictionary)
ucs(initial_order, dictionary)

# Validation
permutations = permute(initial_order)
costs = [calculate_cost(order, dictionary) for order in permutations]
min_cost = min(costs)
best_order = permutations[costs.index(min_cost)]

print(f"\nBest Order: {best_order}, Minimum Cost: {min_cost}")
