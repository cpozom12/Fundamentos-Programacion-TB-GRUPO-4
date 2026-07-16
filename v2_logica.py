# --- PSEUDOCODIGO ---
# Entradas: Cantidad de tecnicos (int), Nombre (str), Sueldo por hora (float), Horas extra (float)
# Proceso:
#   1. Iterar segun la cantidad de tecnicos.
#   2. Calcular el pago extra: 25% para las 2 primeras horas, 35% para las horas que excedan.
#   3. Guardar cada tecnico con su pago en un arreglo.
# Salidas: Reporte con el pago de cada tecnico y el total a depositar.

RECARGO_25 = 1.25   # recargo de ley para las 2 primeras horas extra
RECARGO_35 = 1.35   # recargo de ley para las horas que exceden las 2

# 1. DECLARACION DE VARIABLES
cantidad = 0
tecnicos = []        # arreglo donde se van a guardar los tecnicos procesados
nombre = ""
sueldo_hora = 0.0
horas_extra = 0.0
pago = 0.0
total = 0.0

print("=" * 50)
print("   LIQUIDADOR DE HORAS EXTRAS AUTOMATIZADO")
print("=" * 50)

# 2. INPUTS DEL PROCESO
cantidad = int(input("\nCantidad de tecnicos a procesar: "))

# 3. LOGICA DEL PROCESO
for i in range(cantidad):
    print(f"\n--- Tecnico {i + 1} de {cantidad} ---")

    nombre = input("Nombre: ")
    sueldo_hora = float(input("Sueldo por hora base (S/): "))
    horas_extra = float(input("Horas extra trabajadas: "))

    # Regla de ley: 25% para las 2 primeras horas, 35% para el resto
    if horas_extra <= 2:
        pago = horas_extra * sueldo_hora * RECARGO_25
    else:
        pago = (2 * sueldo_hora * RECARGO_25) + ((horas_extra - 2) * sueldo_hora * RECARGO_35)

    tecnicos.append([nombre, horas_extra, round(pago, 2)])

# 4. OUTPUTS DEL PROCESO (version basica, se mejora el formato en la version 3)
print("\nResultados:")
for t in tecnicos:
    print(t)
