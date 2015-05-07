#get all the good stuff going

from tokens import *
from azure.storage import TableService, Entity, QueueService
import random


myaccount = getAccount()
mykey = getKey()

table_service = TableService(account_name=myaccount, account_key=mykey)
queue_service = QueueService(account_name=myaccount, account_key=mykey)


def getAzureTable():
    return table_service

def getAzureQueue():
    return queue_service 

def getMessage():
    messages = queue_service.get_messages('acceldata')
    for message in messages:
        return message.message_text
        queue_service.delete_message('acceldata', message.message_id, message.pop_receipt)

def getDictOfUnicode(x):
    return eval(str(x))

def generateRandom(xyorz):
    if xyorz == 'x':
        return random.randint(0, 9)
    if xyorz == 'y':
        return random.randint(10, 99)
    if xyorz == 'z':
        return random.randint(100, 999)

