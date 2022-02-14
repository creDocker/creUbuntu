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
        
        channel.queue_declare(queue=queueName, durable=True, auto_delete=False)
        channel.basic_consume(queue=queueName,
                      auto_ack=False,
                      on_message_callback=callback)
        threadId = threading.Thread(target=channel.start_consuming)
        threadId.start()
        return threadId
    else:
        print('ATTENTION: receiveQueue failed.')
        return False

def createQueue(exChangeName, bindingKey, queueName):
    parameters = pikaConfig.getPikaParameters()
    if(parameters):
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.exchange_declare(exchange=exChangeName,
                         exchange_type='x-delayed-message',
                         arguments={"x-delayed-type":"direct"})
        queue = channel.queue_declare(queue=queueName, durable=True, auto_delete=False)
        channel.queue_bind(exchange=exChangeName,
                       queue=queueName,
                       routing_key=bindingKey)
    else:
        print('ATTENTION: createQueue failed.')

def sendQueue(exChangeName, messageBody, routingKey, queueName, delayTime=-1):
    parameters = pikaConfig.getPikaParameters()
    if(parameters):
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        createQueue(exChangeName, routingKey, queueName)
        if(delayTime>0.0):
            delay = int(delayTime/1000.0)
            channel.basic_publish(exchange=exChangeName,
                      routing_key=routingKey,
                      properties=pika.BasicProperties(
                          headers={'x-delay': delay} # Add a key/value header
                      ),
                      body=messageBody)
        else:
            channel.basic_publish(exchange=exChangeName,
                      routing_key=routingKey,
                      body=messageBody)
    else:
        print('ATTENTION: sendQueue failed.')


def lengthQueue(queueName):
    length = pikaConfig.getQueueLength(queueName)
    if(length>=0):
        return(length)
    else:
        print('ATTENTION: lengthQueue failed.')
        return -1



# https://python.plainenglish.io/improve-your-code-with-decorators-4fec033b99eb
# https://realpython.com/primer-on-python-decorators/

def log_with_name(name):
  def log_result(f):
    def inner(*args, **kwargs):
      res = f(*args, **kwargs)
      print(name + ": " + str(res))
      return inner
  return log_result


@log_with_name("Sum")
def sum(a, b):
  return a+b


# @receiveFromQueue(q)
# @sendToQueue(q)
# @limitByQueue(q l)
# @loopByTime(t)










