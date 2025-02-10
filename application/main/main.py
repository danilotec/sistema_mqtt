import time
from .mqtt_connection.mqttClientConnection import MqttClientConnection
from application.configs.configs import Config

def start():
    mqtt_client_connection = MqttClientConnection(
        Config().host,
        Config().port,
        Config().clientname,
        Config().username,
        Config().password,
    )
    mqtt_client_connection.start_connection()

    while True: time.sleep(0.001) #matem o client rodando em loop