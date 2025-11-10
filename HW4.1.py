numbers = [1, 0, 13, 0, 0, 0, 5]
new_list = []

for num in numbers[:]:
    if num == 0:
        new_list.append(num)
        numbers.remove(num)

combined = numbers + new_list

print(combined)