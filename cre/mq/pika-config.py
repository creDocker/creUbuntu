import pika

def getPikaParameters():
    #credentials =  pika.credentials.PlainCredentials('user', 'password', erase_on_connect=False)
    #parameters = pika.ConnectionParameters('ip-address', port, '/', credentials)
    parameters = False
    print('ATTENTION: RabbitMQ credentials not set.')
    return parameters

def getPikaQueues():
    queues = []
    print('ATTENTION: RabbitMQ queues not set.')
    return queues

def getQueueLenght(queueName):
    print('ATTENTION: RabbitMQ credentials not set.')
    return -1
