from operaciones import resta,multiplicacion
from geometria import radio_circulo, base_altura_triangulo
from validador import valida,numero_par,valida_contra
from logica import numero_mayor
from evaluador import nota_final
from texto_utils import palabras,valida_palabras,mayuscula,nombres_mayuscula
from conversor import cantida_dolar,clima
from finanzas import producto,iva
from tiempo import hora
from auth import verificar
print("="*60)
print("1.Resta")
print("2.Multiplicacion")
print("3.Circulo (radio)")
print("4.Triangulo (area)")
print("5.Validar de par")
print("6.Validar de positivo o negativo")
print("7.Numero mayor")
print("8.nota")
print("9.contraseña tiene caracteres mas de 8")
print("10.Recibe nombre y apellido")
print("11.cantidad de caracteres")
print("12.primera letra mayuscula")
print("13.si empieza la letra a")
print("14.Conversion de dolar a bs")
print("15.conversion de C a F")
print("16.descuento")
print("17.IVA")
print("18.Cantidad de minutos")
print("19.Valida contraseña y clave")
print("="*60)
op=int(input("INGRESA EL EJERCICIO: "))

match op:
    case 1:
        n1=int(input("INGRESA UN NUMERO PARA RESTAR: "))
        n2=int(input("INGRESA UN NUMERO NUEVO : "))
        print(resta(n1,n2))
    case 2:
        n1=int(input("INGRESA UN NUMERO PARA RESTAR: "))
        n2=int(input("INGRESA UN NUMERO NUEVO : "))
        print(multiplicacion(n1,n2))
    case 3:
        r=float(input("INGRESA LA RADIO DE UN CIRCULO PARA SABER LA AREA: "))
        print(F"EL AREA DE UN CIRCULO ES:{radio_circulo(r):.0f} ")
    case 4:
        b=float(input("INGRESA LA BASE DEL TRIANGULO: "))
        a=float(input("INGRESA LA ALTURA DEL TRIANGULO: "))
        print(f"EL AREA DEL TRIANGULO ES: {base_altura_triangulo(b,a):.0f}")
    case 5:
        n_entero=int(input("INGRESA UN NUMERO DE ENTERO SI ES TRUE O FALSE: "))
        valida(n_entero)
    case 6:
        n_par=int(input("INGRESA UN NUMERO SI ES PAR O IMPAR: "))
        numero_par(n_par)
    case 7:
        num=int(input("INGRESA UN NUMERO PARA VER EL MAYOR: "))
        num1=int(input("INGRESA UN NUMERO PARA VER EL MAYOR:"))
        num2=int(input("INGRESA UN NUMERO PARA VER EL MAYOR: "))
        numero_mayor(num,num1,num2)
    case 8:
        nota=int(input("INGRESA LA NOTA DEL ESTUDIANTE: "))
        nota_final(nota)
    case 9:
        contraseña=input("INGRESA LA CONTRASEÑA: ").strip()
        valida_contra(contraseña)
    case 10:
        nombre=input("INGRESA TU NOMBRE")
        apellido=input("INGRESA TU APELLIDO")
        nombres_mayuscula(nombre,apellido)
    case 11:
        frase=input("INGRESA UNA FRASE: ")
        print(palabras(frase))
    case 12:
        fra=input("INGRESA UNA FRASE: ")
        mayuscula(fra)
    case 13:
        p=input("INGRESA UNAS PALABRAS: ").lower().strip()
        valida_palabras(p)
    case 14:
        dolar=float(input("INGRESA LA CANTIDAD DE DOLARES PARA QUE TE MUESTRE LOS BS: "))
        print(cantida_dolar(dolar))
    case 15:
        temperatura=int(input("INGRESA LA TEMPERATURA EN GRADOS CELSIUS PARA CONVERTIR A F: "))
        print(clima(temperatura),"F")
    case 16:
        precio=float(input("INGRESA EL PRECIO DEL PRODUCTO: "))
        descuento=int(input("INGRESA EL DESCUENTO APLICAR: "))
        producto(precio,descuento)
    case 17:
        impuesto=int(input("INGRESA EL MONTO DEL IMPUESTO: "))
        iva(impuesto)
    case 18:
        horas=int(input("INGRESA LA CANTIDAD DE HORAS: "))
        print(hora(horas),"minutos")
    case 19:
        usuario=input("INGRESA EL USUARIO: ").strip().lower()
        clave=input("INGRESA LA CLAVE: ").strip()

        verificar(usuario,clave)
    case _:
        print("no hay mas opciones que de 1,19")
