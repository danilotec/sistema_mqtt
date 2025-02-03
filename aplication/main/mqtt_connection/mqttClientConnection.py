import paho.mqtt.client as mqtt


class MqttClientConnection:
    def __init__(self, 
                broker: str, port: int, 
                client_name: str, username: str,
                password: str, keepalive=60) -> None:
        self.__broker = broker
        self.__port = port
        self.__client_name = client_name
        self.__keepalive = keepalive
        self.__username = username
        self.__password = password

    def start_connection(self):
        mqtt_client = mqtt.Client(self.__client_name) #type: ignore

        mqtt_client.connect(host=self.__broker, port=self.__port,
                            keepalive=self.__keepalive)
        mqtt_client.loop_start()