import asyncio
async def mi_Corrutina():
    print("Comenzamos a esperar")
    await asyncio.sleep(3)
    print("Espere 3 segundotes a que me respondiera mi api")
    
# En Python, las corrutinas definidas con async def no se ejecutan 
# directamente al ser llamadas; en su lugar, necesitas usar un bucle de eventos para ejecutarlas
asyncio.run(mi_Corrutina())



async def tarea(numero):
    print(f"Comenzando tarea {numero}")
    await asyncio.sleep(1)
    print(f"Terminando tarea {numero}")

async def main():
    await asyncio.gather(tarea(1), tarea(2), tarea(3))

asyncio.run(main())