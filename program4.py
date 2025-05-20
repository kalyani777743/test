

Numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

result = {i: 0 for i in range(1, 10)}

for i in range(1, 10):
    for num in Numbers:
        if num % i == 0:
            result[i] += 1

print(result)
