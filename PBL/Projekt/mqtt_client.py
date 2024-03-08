import paho.mqtt.client as mqtt
import json
import time
import random

# MQTT broker settings
broker_address = "127.0.0.1"
broker_port = 1883
topic = "sensor-data"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection")

# Create an MQTT client instance
client = mqtt.Client()

# Set the callbacks
client.on_connect = on_connect
client.on_disconnect = on_disconnect

# Connect to the broker
client.connect(broker_address, broker_port, 60)

# Start the MQTT client loop
client.loop_start()

try:
    while True:
        # Generate sample data
        data = {
            "device_id": "123",
            "Audio_level": random.uniform(1, 10),
            "RDS_PI": random.randint(1000, 9999),
            "RDS_RT": f"Station {random.randint(1, 10)}",
            "RSSI": random.uniform(-50, -90),
            "status-code": random.randint(0, 1),
        }

        # Convert data to JSON
        payload = json.dumps(data)

        # Publish the data to the topic
        client.publish(topic, payload)

        print("Data sent:", payload)

        # Wait for a while before sending the next data
        time.sleep(5)

except KeyboardInterrupt:
    print("Script terminated by user")

finally:
    # Disconnect from the broker when the script is terminated
    client.disconnect()
    client.loop_stop()