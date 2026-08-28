def verificar(usuario,clave):
    if usuario == "admin" and clave == "1234":
        print(True)
        print("ACCESO CONCEDIDO")
    else:
        print(False)
        print("ACCESO DENEGADO")