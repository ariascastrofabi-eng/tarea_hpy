def palabras(palabra):
    return len(palabra)
def valida_palabras(p):
    if p[0] == "a":
        print(True)
    else:
        print(False)
def mayuscula(pa):
    no=pa.capitalize()
    print(no)
def nombres_mayuscula(nombres,apellidos):
    print(f"{nombres} {apellidos}")