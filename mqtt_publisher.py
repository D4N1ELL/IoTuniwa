import paho.mqtt.client as mqtt
import random
import time
import json

# MQTT Configurations
BROKER_ADDRESS = "192.168.2.18" 
PORT = 1883 
Topic = "sensor"  

def main():
    
    client = mqtt.Client()
    
    client.connect(BROKER_ADDRESS, PORT, keepalive=60)
    print(f"Connected to MQTT broker at {BROKER_ADDRESS}:{PORT}")
    
    while True:
    
        temperature = round(random.uniform(0.0, 60.0), 2)
        humidity = round(random.uniform(0.0, 100.0), 2)   

            
        sensor_message = json.dumps({
            "temperature": {
                "value": temperature,
                "unit": "Celsius"
            },
            "humidity": {
                "value": humidity,
                "unit": "%"
            }
        })
        
        client.publish(Topic, sensor_message)
        print(f"Published to {Topic}: {sensor_message}")

        time.sleep(1) 

if __name__ == "__main__":
    main()
