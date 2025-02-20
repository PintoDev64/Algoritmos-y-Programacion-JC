Chelines = float(input("Ingrese la cantidad en chelines austriacos: "))
ToPesetas = (Chelines * 956.871) / 100
print(f"{Chelines} chelines austriacos equivalen a {ToPesetas} pesetas.")

Dracmas = float(input("Ingrese la cantidad en dracmas griegos: "))
ToPesetas = (Dracmas * 88.607) / 100
ToFrancos = ToPesetas / 20.110
print(f"{Dracmas} dracmas griegos equivalen a {ToFrancos} francos franceses.")

Pesetas = float(input("Ingrese la cantidad en pesetas: "))
ToDollars = Pesetas / 122.499
ToLibras = (Pesetas * 100) / 9.289
print(f"{Pesetas} pesetas equivalen a {ToDollars} dólares y {ToLibras} liras italianas.")
