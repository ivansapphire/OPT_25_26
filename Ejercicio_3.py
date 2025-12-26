usuario_correcto = "admin"
contrasena_correcta = "1234"

usuario = input("Usuario: ")
contrasena = input("Contraseña: ")

if (usuario == usuario_correcto) and (contrasena == contrasena_correcta):
    print("Correcto")
else:
    print("Incorrecto")