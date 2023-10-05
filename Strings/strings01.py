name = input("Enter your full name : ")
result = len(name)
space = name.find("o") #first ocurrence
space2 = name.rfind("q") #last ocurrence
name2 = name.capitalize() #Solo hace capital la primera
name3 = name.upper() # Todo en letra capital
name4 = name.lower() # Todo en letra minuscula
name5 = name.isdigit() # Solo retorna true si hay digitos en el string
name6 = name.isalpha() #Depende si solo hay letras nos retorna True osea valores alfanumericos

print(result)
print(space)
print(space2)
print(name2)
print(name3)
print(name4)
print(name5)
print(name6)