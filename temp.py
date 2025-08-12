import requests
import random
import time

# Lista de IDs de andenes
platform_ids = [1, 2, 3, 4]

# URL base
# BASE_URL = "http://telemetriaperu.com:7079/api/v1/platforms/temperature/"
BASE_URL = "http://192.168.0.204:7079/api/v1/platforms/temperature/"
# Tiempo de espera entre ciclos (segundos)
CYCLE_INTERVAL = 10

while True:
    for platform_id in platform_ids:
        # Generar temperatura aleatoria con 1 decimal
        temperature = round(random.uniform(15.5, 40.8), 1)

        # URL completa
        url = f"{BASE_URL}{platform_id}"

        # JSON a enviar
        payload = {
            "temperature": temperature
        }

        try:
            # Enviar PUT (o POST si tu API lo requiere)
            response = requests.patch(url, json=payload)

            if response.status_code == 200:
                print(f"✅ Plataforma {platform_id}: temperatura {temperature}°C enviada correctamente.")
            else:
                print(f"⚠️ Plataforma {platform_id}: error {response.status_code} - {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"❌ Error de conexión para plataforma {platform_id}: {e}")

    # Esperar antes del siguiente ciclo
    print(f"⏳ Esperando {CYCLE_INTERVAL} segundos antes del siguiente envío...")
    time.sleep(CYCLE_INTERVAL)
