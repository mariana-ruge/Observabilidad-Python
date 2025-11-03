# scripts/generate_traffic.py

'''
Genera un tráfico continúo HTTP hacia una url (en este caso, localhost:8000)
Simula las peticiones de un servidor
'''

#Importa librerias
import requests
import time
import random

#Url donde se abre el puerto de despliegue del contenedor
BASE_URL = "http://localhost:8000"

endpoints = ["/", "/slow"]

#Simulador del trafico
print("Generando tráfico... Presiona Ctrl+C para detener.")
try:
    while True:
    #Escoge los endpoints para la conexión
        endpoint = random.choice(endpoints)
        try:
            res = requests.get(f"{BASE_URL}{endpoint}", timeout=5)
            print(f"✅ {endpoint} -> {res.status_code}")
        except Exception as e:
            print(f"❌ Error en {endpoint}: {e}")
        time.sleep(random.uniform(0.5, 2.0))
except KeyboardInterrupt:
    print("\nTráfico detenido.")