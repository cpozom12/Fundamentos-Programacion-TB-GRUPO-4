# =====================================================================
# LIQUIDADOR DE HORAS EXTRAS AUTOMATIZADO - VERSION 4 VALIDADA
# Grupo 4 - Fundamentos de Programacion 1
#
# Mejoras frente a v3_final.py:
# 1. Valida que la cantidad de tecnicos sea un entero positivo.
# 2. Valida que el nombre no quede vacio.
# 3. Valida que sueldo por hora y horas extra no sean negativos.
# 4. Usa Decimal para redondeo monetario correcto a 2 decimales.
# 5. Mantiene estructuras basicas: variables, condicionales, bucles,
#    arreglos/listas, funciones, entrada y salida por consola.
# =====================================================================

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

RECARGO_25 = Decimal("1.25")   # Pago normal + 25% de recargo
RECARGO_35 = Decimal("1.35")   # Pago normal + 35% de recargo
DOS_DECIMALES = Decimal("0.01")


def redondear_monto(monto):
    """Redondea un monto monetario a 2 decimales."""
    return monto.quantize(DOS_DECIMALES, rounding=ROUND_HALF_UP)


def leer_entero_positivo(mensaje):
    """Pide un numero entero positivo hasta que el usuario lo ingrese bien."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("  >> Ingrese un numero entero mayor que cero.")
            else:
                return valor
        except ValueError:
            print("  >> Ingrese solo numeros enteros.")


def leer_texto_obligatorio(mensaje):
    """Pide un texto y valida que no este vacio."""
    while True:
        texto = input(mensaje).strip().title()
        if texto == "":
            print("  >> El nombre no puede quedar vacio.")
        else:
            return texto


def leer_decimal_no_negativo(mensaje):
    """Pide un numero decimal mayor o igual que cero."""
    while True:
        try:
            valor = Decimal(input(mensaje).strip())
            if valor < 0:
                print("  >> El valor no puede ser negativo.")
            else:
                return valor
        except InvalidOperation:
            print("  >> Ingrese un numero valido.")


def calcular_pago_extra(sueldo_hora, horas_extra):
    """Calcula el pago de horas extra aplicando 25% y 35% segun la ley."""
    if horas_extra <= 2:
        pago = horas_extra * sueldo_hora * RECARGO_25
    else:
        pago = (
            Decimal("2") * sueldo_hora * RECARGO_25
            + (horas_extra - Decimal("2")) * sueldo_hora * RECARGO_35
        )

    return redondear_monto(pago)


# ---------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------------
tecnicos = []
total = Decimal("0.00")

print("=" * 55)
print("      LIQUIDADOR DE HORAS EXTRAS AUTOMATIZADO")
print("=" * 55)

cantidad = leer_entero_positivo("\nCantidad de tecnicos a procesar: ")

for i in range(cantidad):
    print(f"\n--- Tecnico {i + 1} de {cantidad} ---")

    nombre = leer_texto_obligatorio("Nombre: ")
    sueldo_hora = leer_decimal_no_negativo("Sueldo por hora base (S/): ")
    horas_extra = leer_decimal_no_negativo("Horas extra trabajadas: ")

    pago = calcular_pago_extra(sueldo_hora, horas_extra)
    tecnicos.append([nombre, horas_extra, pago])

print("\n" + "=" * 55)
print("             REPORTE DE PAGO - HORAS EXTRAS")
print("=" * 55)

for nombre, horas_extra, pago in tecnicos:
    print(f"{nombre:<22} {horas_extra} h extra   S/ {pago:.2f}")
    total += pago

print("-" * 55)
print(f"TOTAL A DEPOSITAR: S/ {total:.2f}")
