credit_number = "1234-4563-7839-2313"
#print(credit_number[:4])
#print(credit_number[5:9])
#print(credit_number[5:])
#print(credit_number[-4])
#print(credit_number[::3])

last_digits = credit_number[-4:]
print(f"XXX-XXXX-XXXX-{last_digits}")

#invertirlo

credit_number = credit_number[::-1]
print(credit_number)