import paho.mqtt.client as mqtt
pub_client=mqtt.Client()
pub_client.connect('broker.hivemq.com',1883)
print("broker connected")
pub_client.publish('38/47','hello')
