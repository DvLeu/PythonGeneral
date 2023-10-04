age = int(input("Enter your age "))

if  age >= 100:
    print("You are to old to sign up! ")
elif age >= 18:
    print("You are now signed up ! ")
elif age < 0:
    print("You havent been born yet !")
else:
    print("Youre not allowed to be here, you must be 18+ to enter !")