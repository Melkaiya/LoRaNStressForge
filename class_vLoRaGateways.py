#class_vLoRaGateways.py
'''
Virtual LoRaWAN Gateway:
    VLoRaGateway represents a virtual LoRaWAN gateway that can connect to an MQTT-based
    LoRaWAN Network Server (LNS). It allows simulation and testing of gateway interactions
    with an LNS.
'''
import paho.mqtt.client as mqtt

class VLoRaGateways:
    def __init__(self, gateway_eui, server_user, server_password, latitude, longitude, altitude, frequency_bands,
                 server_address, server_port, gateway_profile, gateway_key, packet_forwarder_protocol, temperature):
        # Initialize gateway attributes

        # MQTT client
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.username_pw_set(username=server_user, password=server_password)
        self.mqtt_client.on_connect = self.on_mqtt_connect
        self.mqtt_client.on_disconnect = self.on_mqtt_disconnect

        # MQTT server details
        self.server_address = server_address
        self.server_port = server_port

        # Connect to the MQTT broker
        self.mqtt_client.connect(server_address, server_port)

    def on_mqtt_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
            # Subscribe to MQTT topics if needed
            # client.subscribe("your_topic")
        else:
            print(f"Failed to connect to MQTT broker with error code {rc}")

    def on_mqtt_disconnect(self, client, userdata, rc):
        if rc != 0:
            print(f"Disconnected from MQTT broker with error code {rc}")
        else:
            print("Disconnected from MQTT broker")

    def connect_to_network_server(self):
        # Connect to the LoRaWAN Network Server
        self.mqtt_client.loop_start()

    def send_data(self, data):
        # Publish data to the MQTT topic
        self.mqtt_client.publish("your_topic", data)

    def disconnect_from_network_server(self):
        # Disconnect from the LoRaWAN Network Server
        self.mqtt_client.loop_stop()
        self.mqtt_client.disconnect()