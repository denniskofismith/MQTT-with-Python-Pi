import paho.mqtt.client as mqtt

def on_connect(client,userdata,flags,rc):
    print(f"Connected with result code {str(rc)} ")


    client.subscribe("")