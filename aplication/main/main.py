import time
from .mqtt_connection.mqttClientConnection import MqttClientConnection
from aplication.configs.mqttBrokerConfigs import mqtt_broker_configs

def start():
    mqtt_client_connection = MqttClientConnection(
        mqtt_broker_configs['HOST'],
        mqtt_broker_configs['PORT'],
        mqtt_broker_configs['CLIENT_NAME'],
        mqtt_broker_configs['USERNAME'],
        mqtt_broker_configs['PASSWORD'],
        mqtt_broker_configs['KEEPALIVE'],
    )
    mqtt_client_connection.start_connection()

    while True: time.sleep(0.001) #matem o client rodando em loop