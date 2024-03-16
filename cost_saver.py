import heapq


def min_cost_to_merge_cables(cables):
    if not cables:
        return 0

    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        shortest_cable1 = heapq.heappop(cables)
        shortest_cable2 = heapq.heappop(cables)

        merged_length = shortest_cable1 + shortest_cable2
        total_cost += merged_length

        heapq.heappush(cables, merged_length)

    return total_cost


def print_cables(cables):
    print("Initial cable list:", cables)

    min_total_cost = min_cost_to_merge_cables(cables)
    print("Minimum cost to merge cables:", min_total_cost)
