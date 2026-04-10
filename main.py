# 11
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

res = list(map(lambda x, y: x * y, a, b))
print(res)

# 12
roy = ["salom123", "python!@#", "2025yil", "test_45"]
print(roy)

res = list(map(lambda el: el.join(filter(str.isalpha))))
print(res)

# 13
roy = [2, 3, 4, 5, 10]

res = list(map(lambda x: x ** roy, roy))
print(res)

# 14
roy = ["nimagap", "yaxshimisan", "ishlaring_qanday"]
print(roy)

res = list(map(lambda el: el.append("!"), roy))
print(res)

# 15
roy1 = [1, 2, 3]
roy2 = [4, 5, 6]
roy3 = [7, 8, 9]
new_roy = roy1 + roy2 + roy3
print(new_roy)

res = list(map(lambda el: sum(el) * 9, new_roy))

# 16
roy = [1, 2, 3]
print(roy)

res = list(map(lambda el: el / 3, roy))
print(res)

# 17
roy = ["JAMSHID"]
print(roy)

res = list(map(lambda el: el.lower, roy))
print(res)

# 18
roy = [0.1, 0.25, 0.5, 0.75, 0.9]
print(roy)

res = list(map(lambda x: int(x * 100), roy))
print(res)

# 19
roy = ["olma", "banan", "gilos", "mandarin", "apelsin"]
print(roy)

res = list(map(lambda s: s[-1], roy))
print(res)

# 20
roy = [5, 10, 15, 255, 1024]
print(roy)

res = list(map(lambda x: bin(x)[2:], roy))
print(res)
