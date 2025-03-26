saldo = 1000

while True:
    print("\n=== Cajero Automático ===")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        deposito = float(input("Ingrese el monto a depositar: "))
        if deposito > 0:
            saldo += deposito
            print(f"Depósito exitoso. Saldo actual: ${saldo:.2f}")
        else:
            print("Monto inválido. Intente nuevamente.")

    elif opcion == "2":
        retiro = float(input("Ingrese el monto a retirar: "))
        if retiro > 0 and retiro <= saldo:
            saldo -= retiro
            print(f"Retiro exitoso. Saldo actual: ${saldo:.2f}")
        elif retiro > saldo:
            print("Fondos insuficientes.")
        else:
            print("Monto inválido. Intente nuevamente.")

    elif opcion == "3":
        print(f"Su saldo actual es: ${saldo:.2f}")

    elif opcion == "4":
        print("Gracias por usar el cajero automático. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intente nuevamente.")