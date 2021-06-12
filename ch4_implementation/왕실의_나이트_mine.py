position = input()

x = int(position[1])
y = int(ord(position[0])) - int(ord('a')) + 1

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

result = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or nx > 8 or ny < 1 or nx > 8:
        continue

    result += 1

print(result)