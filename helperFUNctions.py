#get all the good stuff going

from tokens import *
from azure.storage import TableService, Entity, QueueService
import random


myaccount = getAccount()
mykey = getKey()

table_service = TableService(account_name=myaccount, account_key=mykey)
queue_service = QueueService(account_name=myaccount, account_key=mykey)

queueName = 'acceldata'
tableName = 'accel4'

def getAzureTable():
    '''returns table_service object of current storage account in use'''
    return table_service

def getTableName():
    '''get string of current working table'''
    return tableName

def getAzureQueue():
    '''returns QueueService object of current storage account in use'''
    return queue_service 

def getQueueName():
    '''returns string of current working queue'''
    return queueName

def getMessage():
    messages = queue_service.get_messages(getQueueName())
    for message in messages:
        messageText = message.message_text
        queue_service.delete_message(getQueueName(), message.message_id, message.pop_receipt)
        return messageText

def getDictOfUnicode(x):
    return eval(str(x))

def generateRandom(xyorz):
    if xyorz == 'x':
        return random.randint(0, 9)
    if xyorz == 'y':
        return random.randint(10, 99)
    if xyorz == 'z':
        return random.randint(100, 999)

def getQueueCount():
    queue_metadata = queue_service.get_queue_metadata(getQueueName())
    return queue_metadata['x-ms-approximate-messages-count']