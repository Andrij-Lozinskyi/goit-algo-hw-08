import heapq

def min_cost_to_connect_cables(cable_lengths):
    heapq.heapify(cable_lengths)
    total_cost = 0
    while len(cable_lengths) > 1:
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        combined = first + second
        total_cost += combined
        heapq.heappush(cable_lengths, combined)
    return total_cost

def main():
    cable_lengths = [5, 4, 2, 8]
    print("Minimal cost to connect cables:", min_cost_to_connect_cables(cable_lengths))

if __name__ == "__main__":
    main()