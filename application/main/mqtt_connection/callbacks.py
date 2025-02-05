from application.configs.mqttBrokerConfigs import mqtt_broker_configs
from application.main.messages.clientMessages import messages_client

def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print(f'Cliente conectado com sucesso: {client}')
        client.subscribe(mqtt_broker_configs['TOPICS'])
    else:
        print(f'Erro ao conectar! codigo={rc}')

def on_subscribe(client, userdata, mid, granted_qos, properties):
    print(f'Client Subscribed at {mqtt_broker_configs['TOPICS']}')
    print(f'QOS: {granted_qos}')

def on_message(client, userdata, message):
    print('\nMensagem recebida!')
    
    message_dict = (f'message: {message.payload}\
                    Time:{message.timestamp}')
    messages_client(message_dict, message.topic)
