n = int(input())
arr = list(map(int, input().split()))[:n]

z = max(arr)

while max(arr) == z:
    arr.remove(z)

print(max(arr))
