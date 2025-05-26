import paho.mqtt.client as mqtt

channel_id = "2970255"
mqtt_host = "mqtt3.thingspeak.com"
mqtt_port = 1883

read_api_key = "YXPHDJOFH6M7LX95"  # kosongkan "" jika channel public

mqtt_username = "KTkyMxETEAUJKTsJCS00DRU"
mqtt_password = "iPTfxLiyptBdIMOYG8ZzIEOX"

topic1 = f"channels/{channel_id}/subscribe/fields/field1"
topic2 = f"channels/{channel_id}/subscribe/fields/field2"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Terhubung ke MQTT ThingSpeak")
        client.subscribe("channels/2970255/subscribe/fields/field1")
        client.subscribe("channels/2970255/subscribe/fields/field2")

        print(f"📡 Menunggu data dari topik:\n - {topic1}\n - {topic2}")
    else:
        print(f"❌ Gagal koneksi, kode: {rc}")


def on_message(client, userdata, msg):
    print(f"📥 Topik: {msg.topic} | Data: {msg.payload.decode()}")

client = mqtt.Client(client_id=mqtt_username)
client.username_pw_set(mqtt_username, mqtt_password)

client.on_connect = on_connect
client.on_message = on_message

print("🔌 Menghubungkan ke MQTT broker...")
client.connect(mqtt_host, mqtt_port, 60)

client.loop_forever()
