row = int(input("How many rows ? : "))
columns = int(input("How many columns ? : "))
symbol = input("Enter a symbol to use : ")
for i in range(row):
    for j in range(columns):
        print(symbol, end="")
    print()
