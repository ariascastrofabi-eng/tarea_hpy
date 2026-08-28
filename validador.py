def valida(a):
    if a > 0:
        print(True)
    else:
        print(False)
def numero_par(a):
    if a % 2 == 0:
        print("numero par")
    elif a < 0:
        print("no hay numeros negativos")
    else:
        print("numero impar")

def valida_contra(contraseña):
    if len(contraseña) >= 8:
        print(True)
    else:
        print(False)