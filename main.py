from operaciones import resta,multiplicacion
from geometria import radio_circulo, base_altura_triangulo
from validador import valida,numero_par,valida_contra
from logica import numero_mayor
from evaluador import nota_final
from texto_utils import palabras,valida_palabras
from conversor import cantida_dolar,clima
from finanzas import producto,iva
from tiempo import hora
from auth import verificar
n1=int(input("INGRESA UN NUMERO PARA RESTAR: "))
n2=int(input("INGRESA UN NUMERO NUEVO : "))
print(resta(n1,n2))
n1=int(input("INGRESA UN NUMERO PARA RESTAR: "))
n2=int(input("INGRESA UN NUMERO NUEVO : "))
print(multiplicacion(n1,n2))
r=float(input("INGRESA LA RADIO DE UN CIRCULO PARA SABER LA AREA: "))
print(F"EL AREA DE UN CIRCULO ES:{radio_circulo(r):.0f} ")
b=float(input("INGRESA LA BASE DEL TRIANGULO: "))
a=float(input("INGRESA LA ALTURA DEL TRIANGULO: "))
print(f"EL AREA DEL TRIANGULO ES: {base_altura_triangulo(b,a):.0f}")
n_entero=int(input("INGRESA UN NUMERO DE ENTERO SI ES TRUE O FALSE: "))
valida(n_entero)
n_par=int(input("INGRESA UN NUMERO SI ES PAR O IMPAR: "))
numero_par(n_par)
num=int(input("INGRESA UN NUMERO PARA VER EL MAYOR: "))
num1=int(input("INGRESA UN NUMERO PARA VER EL MAYOR:"))
num2=int(input("INGRESA UN NUMERO PARA VER EL MAYOR: "))
numero_mayor(num,num1,num2)
nota=int(input("INGRESA LA NOTA DEL ESTUDIANTE: "))
nota_final(nota)
contraseña=input("INGRESA LA CONTRASEÑA: ").strip()
valida_contra(contraseña)
frase=input("INGRESA UNA FRASE: ")
print(palabras(frase))
p=input("INGRESA UNAS PALABRAS: ").lower().strip()
valida_palabras(p)
dolar=float(input("INGRESA LA CANTIDAD DE DOLARES PARA QUE TE MUESTRE LOS BS: "))
print(cantida_dolar(dolar))
temperatura=int(input("INGRESA LA TEMPERATURA EN GRADOS CELSIUS PARA CONVERTIR A F: "))
print(clima(temperatura),"F")
precio=float(input("INGRESA EL PRECIO DEL PRODUCTO: "))
descuento=int(input("INGRESA EL DESCUENTO APLICAR: "))
producto(precio,descuento)

impuesto=int(input("INGRESA EL MONTO DEL IMPUESTO: "))
iva(impuesto)

horas=int(input("INGRESA LA CANTIDAD DE HORAS: "))
print(hora(horas))

usuario=input("INGRESA EL USUARIO: ").strip().lower()
clave=input("INGRESA LA CLAVE: ").strip()

verificar(usuario,clave)

