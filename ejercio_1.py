listas_de_temperaturas = [18, 25, 31, 12, 28, 35, 20]

frias = 0
templaddas = 0
calurosas = 0

for temperatura in listas_de_temperaturas:
    if temperatura < 20:
        frias += 1
    elif 20 <= temperatura <= 30:
        templaddas += 1
    else:
        calurosas += 1
    print(f"Temperatura: {temperatura}°C")

    resultado = f"Clasificación de temperaturas"
    f"\nFrías: {frias}\n"
    f"Templadas: {templaddas}\n"
    f"Calurosas: {calurosas}"
    print(resultado)