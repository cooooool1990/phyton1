numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
new_list = []

for num in numbers[:]:
    if num == 0:
        new_list.append(num)
        numbers.remove(num)

combined = numbers + new_list

print(combined)