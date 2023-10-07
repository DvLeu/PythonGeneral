age = int(input("Enter your age : "))

while age < 0:
    print("Age cant be negative ")
    age = int(input("Enter your age : "))

print(f"Age is : {age}")