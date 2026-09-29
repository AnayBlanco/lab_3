def sumar(primer_numero, segundo_numero):
    return primer_numero + segundo_numero


def restar(primer_numero, segundo_numero):
    return primer_numero - segundo_numero


def multiplicar(primer_numero, segundo_numero):
    return primer_numero * segundo_numero


def dividir(primer_numero, segundo_numero):
    resturn primer_numero / segundo_numero


def es_par(numero):
    pass


while True:
    print("\n--- CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Verificar si un número es par")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    # Completa aquí usando match/case.