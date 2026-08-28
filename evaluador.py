def nota_final (nota):
    if nota > 100 or nota < 0:
        print("NOSE PUEDE PONER OTROS NUMEROS MAYORES A 100 O MENORES A 0")
    else:
        if nota >= 51:
            print("APROBADO")
        else:
            print("REPROBADO")