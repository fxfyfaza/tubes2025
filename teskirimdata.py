import requests
import time
import random

# GANTI dengan Write API Key dari channel kamu
WRITE_API_KEY = '7DFPC06L1AAX11M9'

# URL endpoint ThingSpeak
url = 'https://api.thingspeak.com/update'

def kirim_data_dummy():
    while True:
        # Data dummy: suhu 20-40 °C dan kecepatan kipas 1000-2000 RPM
        suhu = round(random.uniform(20, 40), 2)
        kipas = random.randint(1000, 2000)

        payload = {
            'api_key': WRITE_API_KEY,
            'field1': suhu,
            'field2': kipas
        }

        response = requests.get(url, params=payload)

        if response.status_code == 200 and response.text != '0':
            print(f'✅ Data terkirim: Suhu={suhu} °C, Kipas={kipas} RPM (entry #{response.text})')
        else:
            print('❌ Gagal kirim data:', response.text)

        time.sleep(15)  # Tunggu 15 detik (ThingSpeak rate limit)
        
if __name__ == "__main__":
    kirim_data_dummy()
