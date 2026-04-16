# Requerimientos
# 1.	Mostrar menú de productos: 
# El programa debe mostrar el siguiente menú:
# 1. Pokébola → $1000
# 2. Poción → $1500
# 3. Revivir → $3000
# 4. Baya → $500
# 5. Finalizar compra
# ________________________________________
# 2.	Ingreso de productos: 
# •	El usuario debe poder seleccionar productos ingresando el número correspondiente. 
# •	Validar que la opción ingresada sea correcta (entre 0 y 4). 
# •	Si la opción es inválida, mostrar un mensaje de error y volver a pedirla. 
# ________________________________________
# 3.	Cantidad de productos: 
# •	Por cada producto seleccionado, pedir la cantidad. 
# •	Validar que la cantidad sea un número entero positivo. 
# ________________________________________
# 4.	Acumulación de compra: 
# •	Calcular el total acumulado de la compra. 
# •	Llevar un contador de la cantidad total de productos comprados. 
# ________________________________________
# 5.	Sistema de descuentos: 
# Aplicar los siguientes descuentos:
# •	🔹 Si el total de la compra supera los $5000 → aplicar 10% de descuento. 
# •	🔹 Si compra más de 10 productos en total → aplicar un 5% adicional. 
# •	🔹 Si el entrenador compra al menos 3 “Revivir” → aplicar un 15% adicional SOLO sobre ese producto. 
#  Los descuentos son acumulables.
# ________________________________________
# 6.	Uso de bandera (flag): 
# •	Usar una bandera para verificar si el usuario compró al menos un producto antes de finalizar. 
# •	Si no compró nada, mostrar un mensaje:
# "No has realizado ninguna compra." 
# ________________________________________
# 7.	Manejo de errores: 
# •	Utilizar try-except para evitar que el programa se rompa ante entradas inválidas (por ejemplo, letras en vez de números). 
# ________________________________________
# 8.	Salida final:
# Mostrar un resumen con: 
# •	Total bruto 
# •	Total de descuentos aplicados 
# •	Total final a pagar 
# •	Cantidad total de productos comprados 

precio_pokebola = 1000
precio_pocion = 1500
precio_revivir = 3000
precio_baya = 500

total_bruto = 0
cantidad_total = 0
cantidad_revivir = 0
compro_algo = False

while True:
    
    print("----------- TIENDA POKEMON -----------")
    print("1. Pokebola -> $1000")
    print("2. Pocion -> $1500")
    print("3. Revivir -> $3000")
    print("4. Baya -> $500")
    print("5. Finalizar Compra")
    
    while True:
        try:
            opcion = int(input("Ingrese una opcion(1-5): "))
            if opcion >= 1 and opcion <= 5:
                break
            else:
                print("¡ERROR! Opcion invalida, intente nuevamente")
        except:
            print("Solo datos numericos")
    
    if opcion == 5:
        break
    
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            
            if cantidad > 0:
                break
            else:
                print("La cantidad debe ser mayor a 0")
        except:
            print("Solo datos numericos positivos")
    
    compro_algo = True
    cantidad_total += cantidad
    
    if opcion == 1:
        total_bruto = precio_pokebola * cantidad
    elif opcion == 2:
        total_bruto = precio_pocion * cantidad
    elif opcion == 3:
        total_bruto = precio_revivir * cantidad
        cantidad_revivir = cantidad
    elif opcion == 4:
        total_bruto = precio_baya * cantidad
    
    










































































