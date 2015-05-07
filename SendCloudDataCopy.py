from azure.storage import TableService, Entity, QueueService
import time
import redis
from tokens import *

myaccount = getAccount()
mykey = getKey()

table_service = TableService(account_name=myaccount, account_key=mykey)
queue_service = QueueService(account_name=myaccount, account_key=mykey)

queue_service.create_queue('acceldata')

i = 0

TableSlotList = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, )

periods = ('a', 'b', 'c', 'd')

#table_service.insert_or_replace_entity(accel2, accel, tableSlot, periodSlot)

record = {}

def analog_read(channel):
    if channel == 0:
        return 0
    if channel == 1:
        return 1
    if channel == 2:
        return 2

while True:
    for tableSlot in TableSlotList:
        for abcd in periods:
            time.sleep(0.1)
            record.update({abcd+'X': analog_read(0), abcd+'Y': analog_read(1), abcd+'Z': analog_read(2)})
        print record

        table_service.insert_or_replace_entity('accel4', 'slot', tableSlot, record)
        queue_service.put_message('acceldata', unicode(record))

