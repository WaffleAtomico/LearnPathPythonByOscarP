import gc

# Desactivar la recolección de basura
gc.disable()

# Realizar tareas intensivas en memoria
# (Aquí puedes incluir tu código que consume memoria)

x = 10
while x > 0:
    x -= 1
# Habilitar la recolección de basura nuevamente
gc.enable()

# Forzar la recolección de basura manualmente
n_recolectados = gc.collect()
print(f"Objetos recolectados: {n_recolectados}")
