import pika
import importlib

pikaConfig = importlib.import_module("pika-config")

def clearQueue(queueName):
    parameters = pikaConfig.getPikaParameters()
    if(Parameters):
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_delete(queue=queueName)
    else:
        print('ATTENTION: clearQueue failed.')








