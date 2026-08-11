n = int(input("Enter number of rows: "))

for i in range(n):
    for j in range(3):
        print(chr(65 + j), end=" ")
    print()