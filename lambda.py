add = lambda x, y: x + y
print(add(3, 4))  # ➜ 7

square = lambda x: x ** 2
print(square(5))  # ➜ 25

evens = list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,6]))
print(evens)  # ➜ [2, 4, 6]

squares = list(map(lambda x: x ** 2, [1,2,3,4]))
print(squares)  # ➜ [1, 4, 9, 16]

fruits = ["Apple", "Banana", "Orange"]
lower = list(map(lambda s: s.lower(), fruits))
print(lower)

data = [(1, 30), (2, 10), (3, 20)]
sorted_data = sorted(data, key=lambda t: t[1])
print(sorted_data)  # ➜ [(2, 10), (3, 20), (1, 30)]