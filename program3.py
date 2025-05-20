

a = int(input("Enter a number (a): "))

if a % 2 == 0:
    count = a - 1
else:
    count = a

for i in range(count):
    print(2 * i + 1, end=", " if i < count - 1 else "\n")
