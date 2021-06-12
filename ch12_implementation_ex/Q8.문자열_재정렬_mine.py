s = input()
ns = sorted(s)

num = 0
strings = ""
for i in ns:
    if i.isdigit():
        num += int(i)
    else:
        strings += i

if num != 0:
    strings += str(num)

print(strings)