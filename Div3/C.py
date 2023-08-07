# Function to calculate Rudolf's place in the final table
def calculate_rudolf_place(n, m, h, times):
    max_score = 0
    min_penalty = float('inf')

    # Calculate score and penalty for a given problem order
    def calculate_score_penalty(order):
        score = 0
        penalty = 0
        for problem in order:
            if penalty + times[0][problem] <= h:
                score += 1
                penalty += times[0][problem]
            else:
                break
        return score, penalty

    # Generate all possible problem orders
    def generate_orders(current_order, remaining_problems):
        if not remaining_problems:
            return [current_order]
        orders = []
        for problem in remaining_problems:
            new_order = current_order + [problem]
            remaining = remaining_problems.copy()
            remaining.remove(problem)
            orders += generate_orders(new_order, remaining)
        return orders

    # Calculate score and penalty for all possible orders
    orders = generate_orders([], list(range(m)))
    for order in orders:
        score, penalty = calculate_score_penalty(order)
        if score > max_score or (score == max_score and penalty < min_penalty):
            max_score = score
            min_penalty = penalty

    # Calculate Rudolf's place based on score and penalty
    place = 1
    for i in range(1, n):
        score, penalty = calculate_score_penalty(list(range(m)))
        if (score, penalty) > (max_score, min_penalty):
            place += 1

    return place


# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n, m, h = map(int, input().split())
    times = []
    for _ in range(n):
        times.append(list(map(int, input().split())))

    # Calculate Rudolf's place for the current test case
    place = calculate_rudolf_place(n, m, h, times)
    print(place)
