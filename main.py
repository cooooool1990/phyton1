number = int(input("Введіть 4-х значне число: "))

a = number // 1000
b = (number // 100) % 10
c = (number // 10) % 10
d = number % 10

print(a)
print(b)
print(c)
print(d)