from functools import cache

@cache
class MessagesTopicsData:
    def __init__(self, topic, message) -> None:
        self.topic = topic
        self.message = message

    def add_message_db(self):
        print(self.topic)
        print(self.message)


def messages_client(message, topic):
    # print(topic)
    a = MessagesTopicsData(topic, message)
    a.add_message_db()
