a = int(input())
b = []
end_time = 0
result = 0

for i in range(a):
    b.append(tuple(map(int, input().split(" "))))

b = sorted(b, key=lambda x : (x[1], x[0]))

for x,y in b:
    if end_time <= x:
        end_time = y
        result += 1

print(result)