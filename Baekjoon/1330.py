a, b = map(int, input().split())

def showComparison(a, b):
    if a > b:
        return '>'
    if a < b:
        return '<'
    return '=='

print(showComparison(a, b))