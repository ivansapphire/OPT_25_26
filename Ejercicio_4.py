num1 = int(input("introduce tu primer número"))
num2 = int(input("introduce tu segundo número"))

print(f"Para sumar pulsa 1")
print(f"Para restar pulsa 2")
print(f"Para multiplicar pulsa 3")
print(f"Para dividir pulsa 4")

opt = int(input("Dime la opción  que quieres"))


if (opt ==1):
    print(f"La suma de tus números es {num1 + num2}!")
elif (opt ==2):
    print(f"La resta de tus números es {num1 - num2}!")
elif (opt ==3):
    print(f"La multiplicación de tus números es {num1 * num2}!")
elif (opt ==4):
    print(f"La división de tus números es {num1 / num2}!")

else: print("Opción no válida, el número no es ninguna de las opciones posibles")
