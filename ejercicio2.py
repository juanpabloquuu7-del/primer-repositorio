def menu():
    print(""" 
*** Bienvenido a calcular tu pago *** 
--- Programa ---    
1. Técnico en Sistemas
2. Técnico en Desarrollo de videojuegos
3. Técnico en Animación Digital

--- Becas ---
1. Descuento del 50% sobre el valor matrícula   
2. Descuento del 40% sobre el valor matrícula 
3. Sin beca      
""")


def obtener_precio_base(programa):
    if programa == 1:
        return 800000
    elif programa == 2:
        return 1000000
    elif programa == 3:
        return 1200000
    else:
        return 0


def matricula():
    while True:
        menu()
        try:
            programa = int(input("Seleccione el programa (1-3): "))
            beca = int(input("Ingrese la beca obtenida (1-3): "))

            precio_base = obtener_precio_base(programa)

            if precio_base == 0 or beca not in [1, 2, 3]:
                print("\n Opción inválida.")
                input("Presione cualquier tecla para continuar...")
            else:
                if beca == 1:
                    total_pagar = precio_base * 0.50
                elif beca == 2:
                    total_pagar = precio_base * 0.60
                else:
                    total_pagar = precio_base

                print(f"\nValor a pagar de matrícula es: ${total_pagar:,.0f}")
                input("Presione cualquier tecla para continuar...")

        except ValueError:
            print("\n Debes ingresar números válidos.")
            input("Presione cualquier tecla para continuar...")


matricula()
