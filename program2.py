
a = int(input("Enter a number: "))


output = []
for i in range(a):
    output.append(2 * i + 1)


print("Output:", ", ".join(map(str, output)))
