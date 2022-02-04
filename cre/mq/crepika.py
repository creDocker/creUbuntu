import pika
import importlib
import threading

pikaConfig = importlib.import_module("pika-config")

def clearQueue(queueName):
    parameters = pikaConfig.getPikaParameters()
    if(parameters):
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_delete(queue=queueName)
    else:
        print('ATTENTION: clearQueue failed.')

def stopReceive(threadId):
    threadId.stop()

def receiveQueue(queueName, callback):
    parameters = pikaConfig.getPikaParameters()
    if(parameters):
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.basic_consume(queue=queueName,
                      auto_ack=False,
                      on_message_callback=callback)
        threadId = threading.Thread(target=channel.start_consuming)
        threadId.start()
        return threadId
    else:
        print('ATTENTION: receiveQueue failed.')
        return False

def sendQueue(queueName, exChangeName, messageBody, delayTime=-1):
    parameters = pikaConfig.getPikaParameters()
    if(parameters):
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        if(delayTime>0.0):
            channel.exchange_declare(exchange=exChangeName,
                         exchange_type='x-delayed-message',
                         arguments={"x-delayed-type":"direct"})
        queue = channel.queue_declare(queue=queueName)
        if(delayTime>0.0):
            delay = int(delayTime/1000.0)
            channel.basic_publish(exchange=exChangeName,
                      routing_key=queueName,
                      properties=pika.BasicProperties(
                          headers={'x-delay': delay} # Add a key/value header
                      ),
                      body=messageBody)
        else:
            channel.basic_publish(exchange=exChangeName,
                      routing_key=queueName,
                      body=messageBody)
    else:
        print('ATTENTION: sendQueue failed.')









