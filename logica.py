def numero_mayor(a,b,c):
    if a > b and a > c:
        print(f"numero mayor {a}")
    elif b > a and b > c:
        print(F"numero mayor {b}")
    elif c > a and c > b:
        print(f"numero mayor {c}")
    elif a==b and b==c and c==a:
        print("no hay numeros mayores son iguales")
    else:
        print("no hay negativos en si")