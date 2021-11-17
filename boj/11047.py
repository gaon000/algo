a, b = list(map(int, input().split(' ')))
coins = []
result = 0

for i in range(a):
    coins.append(int(input()))

for i in reversed(coins):
    if b / i >= 1:
        result += b//i
        b = b%i

print(result)