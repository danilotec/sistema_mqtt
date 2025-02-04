import paho.mqtt.client as mqtt
from paho import mqtt as tls_mqtt
from .callbacks import on_connect, on_message, on_subscribe

class MqttClientConnection:
    def __init__(self, 
                broker: str, port: int, 
                client_name: str, username: str,
                password: str, keepalive=60) -> None:
        self.mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2) #type: ignore
        self.__broker = broker
        self.__port = port
        self.__client_name = client_name
        self.__keepalive = keepalive
        self.__mqtt_client = None

        self.mqtt_client.tls_set(tls_version=tls_mqtt.client.ssl.PROTOCOL_TLS) #type: ignore
        self.mqtt_client.username_pw_set(username, password)

    def start_connection(self):
        self.mqtt_client.on_connect = on_connect
        self.mqtt_client.on_subscribe = on_subscribe
        self.mqtt_client.on_message = on_message

        self.mqtt_client.connect(host=self.__broker, port=self.__port,
                            keepalive=self.__keepalive)
        self.mqtt_client.loop_start()
    
    def end_connection(self):
        try:
            self.mqtt_client.loop_stop()
            self.mqtt_client.disconnect()
            return True
        except:
            return False