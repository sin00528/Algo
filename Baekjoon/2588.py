n = int(input())
m = int(input())

print(int(n * (m % 10)))
print(int(n * ((m // 10) % 10)))
print(int(n * (m // 100)))
print(n * m)