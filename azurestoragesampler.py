from pseudoAccelerometer import *
import time
import redis
from tokens import *
from azure.storage import TableService, Entity

myaccount = getAccount()
mykey = getKey()

r = redis.StrictRedis(host='pistate.redis.cache.windows.net', port=6380, db=0, password=getRedisToken, ssl=True)

table_service = TableService(account_name=myaccount, account_key=mykey)

i = 0

TableSlotList = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,43,44,45,46,47,48,49,50)

periods = ('a', 'b', 'c', 'd')


zSlots = ('quarter', 'half', 'threefourths', 'last')

#table_service.insert_or_replace_entity(accel2, accel, tableSlot, periodSlot)

record = {}

#records = {'aX': generateX(),'aY': generateY(),'aZ': generateZ(),'bX': generateX(),'bY': generateY(),'bZ': generateZ(), 'cX': generateX(),'cY': generateY(),'cZ': generateZ(),'cX': generateX(),'cY': generateY(),'cZ': generateZ() }


while True: 

    for tableSlot in TableSlotList:
        for abcd in periods:
            time.sleep(0.1) 
            record.update({abcd+'Z': generateX(), abcd+'Y': generateY(), abcd+'Z': generateZ()})
        print record
        table_service.insert_or_replace_entity('accel4', 'slot', tableSlot, record)

while True: 

    for tableSlot in TableSlotList:
        for abcd in periods:
            time.sleep(0.1) 
            print tableSlot
            print abcd
            print record 
            xValue = generateX()
            yValue = generateY()
            zValue = generateZ()
            record.update({abcd+'Z': xValue, abcd+'Y': yValue, abcd+'Z': zValue})
        table_service.insert_or_replace_entity('accel4', 'slot', tableSlot, record)
    

while True: 
    time.sleep(.1)
    for a in xList: 
        r.set(a+'x', generateX())
        r.set(a+'y', generateY())
        r.set(a+'z', generateZ())
        print a + ' z ' + r.get(a+'z')
        print a + ' y ' + r.get(a+'y')
        print a + ' x ' + r.get(a+'x')

while True: 
    time.sleep(.1)
    r.set('oneEx', generateX())
    r.set('twoEx', generateX())
    print r.get('oneEx')
    

import spidev, time
from azure.storage import TableService, Entity

spi = spidev.SpiDev()
spi.open(0,0)

my_account = 'pipractice'
my_key = 'BJNu+LXFAAoaSYm8GRNmaRcBvyM6OySC9BgKc8fr03Z9myqzVXUHtsJNpsfD7uI9a6PPi1tZwUMvkx9C2z/4Zg=='
table_service = TableService(account_name=my_account, account_key=my_key)

table_service.create_table('accel')

def analog_read(channel):
        r = spi.xfer2([1, (8 + channel) << 4, 0])
        adc_out = ((r[1]&3) << 8) + r[2]
        return adc_out

while True:
        x = analog_read(0)
        y = analog_read(1)
        z = analog_read(2)
        accel = Entity()
        accel.PartitionKey = 'accelValue'
        accel.RowKey = '1'
        accel.x = x
        accel.y = y
        accel.z = z
        table_service.insert_or_replace_entity('accel', 'accelValue', '1',  accel)

        print("X=%d\tY=%d\tZ=%d" %(x, y, z))

        #accelFrom = table_service.get_entity('accel', 'accelValue', '1')
        #print(accelFrom.x)
        time.sleep(1)



