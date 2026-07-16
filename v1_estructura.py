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

# 3. LOGICA DEL PROCESO (estructura del bucle, se completa en la version 2)
for i in range(cantidad):
    print(f"\n--- Tecnico {i + 1} de {cantidad} ---")
    # Aca falta pedir los datos del tecnico y calcular su pago (ver version 2)

# 4. OUTPUTS DEL PROCESO (se completa en la version 2)
print("\nReporte pendiente de implementar")
