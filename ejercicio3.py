def menu():
    print(""" 
*** Bienvenido al Sistema de Comisiones *** --- Tipo de Vendedor ---    
1. Puerta a Puerta (20% comisión)
2. Telemercadeo (15% comisión)
3. Ejecutivo de ventas (25% comisión)
""")

def calcular_comision(tipo, valor_ventas):
    if tipo == 1:
        return valor_ventas * 0.20
    elif tipo == 2:
        return valor_ventas * 0.15
    elif tipo == 3:
        return valor_ventas * 0.25
    else:
        return 0

def gestion_vendedor():
    
    while True:
        menu()
        try:
            cedula = input("Ingrese Cédula de ciudadanía: ")
            nombre = input("Ingrese nombre del vendedor: ")
            tipo = int(input("Seleccione el tipo de vendedor (1-3): "))
            valor_ventas = float(input("Ingrese el valor de ventas del mes: "))

            comision = calcular_comision(tipo, valor_ventas)

            if comision == 0 and tipo not in [1, 2, 3]:
                print("\n Opción de tipo inválida.")
                input("Presione cualquier tecla para intentar de nuevo...")
            else:
                
                print()
                print("Resumen de liquidacion")
                print(f"Vendedor: {nombre}")
                print(f"Cédula: {cedula}")
                print(f"Ventas del mes: ${valor_ventas:,.0f}")
                print(f"Comisión a pagar: ${comision:,.0f}")
                print()
                
                print("Proceso finalizado con éxito.")
                break 

        except ValueError:
            print("Error: Debes ingresar números válidos.")
            input("Presione cualquier tecla para continuar...")


gestion_vendedor()