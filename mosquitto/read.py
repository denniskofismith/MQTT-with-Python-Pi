import paho.mqtt.client as mqtt

def on_connect(client,userdata,flags,rc):
    print(f"Connected with result code {str(rc)} ")


    client.subscribe("koddy")

# def on_message(client,userdata, msg):
#     print(f"{msg.topic} {\n}  msg.payload.decode("utf-8") {\n}")

def on_message(client, userdata, msg):
    print(msg.topic + " \n " + msg.payload.decode("utf-8") + " \n ")

    

client = mqtt.Client()

client.on_message = on_message
client.on_connect = on_connect

client.connect("0.0.0.0", 1883, 60)

client.loop_forever()