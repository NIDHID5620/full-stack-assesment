a = int(input("Enter the value of a: "))

series = []
for i in range(a):
    series.append(str(2 * i + 1))

print(", ".join(series))
