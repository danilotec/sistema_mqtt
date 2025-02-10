from application.configs.configs import Config
from application.main.messages.clientMessages import MessagesTopicsData
from application.database.base import SessionLocal
from application.main.controller.monitorDevices import IoTMonitoring


def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print(f'Cliente conectado com sucesso: {client}')
        client.subscribe(Config().topics)
    else:
        print(f'Erro ao conectar! codigo={rc}')

def on_subscribe(client, userdata, mid, granted_qos, properties):
    print(f'Client Subscribed at {Config().topics}')
    print(f'QOS: {granted_qos}')

def on_message(client, userdata, message):
    db = SessionLocal()
    message_payload = message.payload.decode()

    message_database = MessagesTopicsData(message.topic, message_payload)
    message_database.add_message_db(db)

    # monitor = IoTMonitoring()
    # monitor.register_message(message.topic)
    # status = monitor.check_devices_status()
    # alerts = monitor.generate_alerts(status)

    