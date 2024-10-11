PRECIO_SENCILLA = 20000
PRECIO_DOBLE = 25000
PRECIO_TRIPLE = 28000
IMPUESTO_TARJETA = 0.07
print("BIENVENIDO A IN-N-OUT BURGER, VOY A TOMAR TU PEDIDO ")

def calcular_precio (tipo_hamburguesa, metodo_pago, cantidad):
    if tipo_hamburguesa == 1:
        precio= PRECIO_SENCILLA
        descripcion = 'sencilla'
    elif tipo_hamburguesa == 2:
        precio = PRECIO_DOBLE
        descripcion = 'doble'
    elif tipo_hamburguesa == 3:
        precio = PRECIO_TRIPLE
        descripcion = 'triple'
    else:
        return None
    total_sin_cargo = precio * cantidad
    if metodo_pago == 1:
        impuesto = round(total_sin_cargo * IMPUESTO_TARJETA)
    else:
        impuesto = 0
    total =round(total_sin_cargo + impuesto)
    return descripcion, precio, cantidad, impuesto, total
def generar_mensaje (descripcion, precio, cantidad, impuesto, total):
    return (f"Tipo hamburguesa: {descripcion}\n"
            f"Precio: ${precio}\n"
            f"Cantidad: {cantidad}\n"
            f"Impuesto: $ {impuesto}\n"
            f"Total: ${total}")
def validar_datos(tipo_hamburguesa, metodo_pago, cantidad):
    if 1 <= tipo_hamburguesa <= 3 and 1 <= metodo_pago <= 2 and cantidad > 0:
        resultado = calcular_precio(tipo_hamburguesa, metodo_pago, cantidad)
        descripcion, precio, cantidad, impuesto, total =resultado
        mensaje = generar_mensaje(descripcion, precio, cantidad, impuesto, total)
        print("---------------------------\n" + mensaje)
    else:
        print("verifique las opciones ingresadas")
cantidad = int(input("Que cantidad de hamburguesas necesitas:\n "))
tipo_hamburguesa = int(input("Que tipo de hamburguesa quieres digita el numero \n1 para Sencilla \n2 para Doble \n3 para triple \n"))
metodo_pago = int(input("Metodo de pago marque: \n1 para tarjeta de credito \n2 para otro medio de pago\n"))

validar_datos(tipo_hamburguesa, metodo_pago, cantidad)
