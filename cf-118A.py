import sys

x = list(sys.stdin.readline().strip().lower())

vowels = ["a", "e", "i", "o", "u", "y"]


x = [_ for _ in x if _ not in vowels]
print("." + ".".join(x))
