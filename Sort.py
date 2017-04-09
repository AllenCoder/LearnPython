print(sorted([36, 5 - 12, 9, -21]))

print(sorted([36, 5, -12, 9, -21], key=abs))

list = [36, 5, -12, 9, -21]
keys = [36, 5, 12, 9, 21]
print(sorted(list))
print(sorted(list, key=str.lower, reverse=True))
