data = input()

sum_val = 0
for i in data:
    sum_val = max(sum_val + int(i), sum_val * int(i))
    
print(sum_val)