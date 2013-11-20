def GCD(a, b):
    if a < b: return GCD(b, a)
    if a % b == 0: return b
    return GCD(b, a % b)

with open('sample.txt') as file:
    for line in file:
        line = line.strip()
        a, b = map(int, line.split(" "))
        print(GCD(a, b))
