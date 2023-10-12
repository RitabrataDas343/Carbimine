import numpy as np
from itertools import permutations

def tsp_held_karp(distance_matrix):
    n = len(distance_matrix)
    all_points = set(range(n))
    
    memo = {}
    
    def min_cost(subset, last):
        if not subset:
            return distance_matrix[last][0]
        
        subset_key = tuple(sorted(subset))
        if (subset_key, last) in memo:
            return memo[(subset_key, last)]
        
        min_distance = float('inf')
        for next_point in subset:
            if next_point != last:
                new_subset = tuple(city for city in subset if city != next_point)
                distance = distance_matrix[last][next_point] + min_cost(new_subset, next_point)
                min_distance = min(min_distance, distance)
        
        memo[(subset_key, last)] = min_distance
        return min_distance
    
    tour = tuple(all_points - {0})
    min_distance = min_cost(tour, 0)
    
    tour = (0,) + tour
    return tour, min_distance

# Get city names from the user
city_names = input("Enter city names separated by spaces: ").split()

# Get the cost matrix from the user
print("Enter the cost matrix (row by row, with values separated by spaces):")
distance_matrix = np.array([list(map(float, input().split())) for _ in range(len(city_names))])

tour, total_cost = tsp_held_karp(distance_matrix)

# Convert city indices to names in the tour
tour_in_names = [city_names[city] for city in tour]

print("TSP Tour:", ' -> '.join(tour_in_names))
print("Total Cost:", total_cost)
