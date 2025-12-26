num1 = int(input("introduce tu primer número"))
num2 = int(input("introduce tu segundo número"))

print(f"Para sumar pulsa 1")
print(f"Para restar pulsa 2")
print(f"Para multiplicar pulsa 3")
print(f"Para dividir pulsa 4")

opt = int(input("Dime la opción  que quieres"))

match opt:
    case  1:
        print(f"La suma de tus números es {num1 + num2}!")
    case 2:
        print(f"La resta de tus números es {num1 - num2}!")
    case  3:
        print(f"La multiplicación de tus números es {num1 * num2}!")
    case 4:
        print(f"La división de tus números es {num1 / num2}!")
    case _:
        print("Opción no válida, el número no es ninguna de las opciones posibles")
