a = int(input("Enter the value of a: "))

if a % 2 == 0:
    count = a - 1
else:
    count = a

series = []
for i in range(count):
    series.append(str(2 * i + 1))

print(", ".join(series))
