n = input()

def showLucky(n):
    mid = len(n) // 2
    front = sum(list(map(int, n[:mid])))
    back = sum(list(map(int, n[mid:])))

    if front == back:
        return 'LUCKY'
    return 'READY'

print(showLucky(n))