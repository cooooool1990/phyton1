lst = [1, 2, 3, 4, 5]  # приклад, можна змінювати

if len(lst) == 0:
    result = [[], []]
else:
    middle = (len(lst) + 1) // 2  # половина списку (з урахуванням непарності)
    result = [lst[:middle], lst[middle:]]

print(result)