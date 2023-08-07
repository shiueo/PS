def is_snowflake_possible(n):
    if n < 4 or n % 2 != 0:
        return "NO"  # Snowflake not possible for n < 4 or odd n

    # Check if n is a power of 2
    if n & (n - 1) != 0:
        return "NO"  # Snowflake not possible if n is not a power of 2

    return "YES"  # Snowflake possible

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    result = is_snowflake_possible(n)
    print(result)
