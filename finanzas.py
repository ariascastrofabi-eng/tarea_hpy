def producto(precio,descuento):
    descuento1=descuento/100
    aplicado=precio*descuento1
    total_pagar=precio-aplicado
    print("TOTAL A PAGAR", total_pagar)

def iva(producto):
    iva1=producto*0.13
    impuesto=producto+iva1
    print("el impuesto total es ",impuesto)