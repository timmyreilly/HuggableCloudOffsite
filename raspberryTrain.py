import time

from tokens import *
from helperFUNctions import *

from azure.storage import TableService, Entity

# ++++ Uncomment this before running on pi: ++++ 

import spidev
spi = spidev.SpiDev()
spi.open(0,0)

myaccount = getAccount()
mykey = getKey()

table_service = TableService(account_name=myaccount, account_key=mykey)

TableSlotNeutral = return_list_generator(0,999)         #n for neutral
TableSlotShaking = return_list_generator(1000, 1999)    #s for shaking
TableSlotSpinning = return_list_generator(2000, 2999)   #sp for spinning
TableSlotPunching = return_list_generator(3000, 3999)    #p for punching
TableSlotHugging = return_list_generator(4000, 4999)     #h for hugging
TableSlotThrowing = return_list_generator(5000, 5999)     #t for thrown

periods = ('a', 'b', 'c', 'd')
record = {}

table_service.create_table(getMLTableName())

# ++++ Uncomment this before running on pi ++++

def analog_read(channel):
        r = spi.xfer2([1, (8 + channel) << 4, 0])
        adc_out = ((r[1]&3) << 8) + r[2]
        return adc_out

#a_r = analog_read

### +++ Comment this out before running on pi ++++

#a_r = generateRandom

while True: 
    x = get_input_type()
    print x
    if x == 'n':
        print 'In 5 seconds start neutral'
        print 'send 1000 points of data to ML set marked neutral'
        time.sleep(5.0)
        print 'START'
        time.sleep(0.5)
        for tableSlot in TableSlotNeutral:
            for abcd in periods:
                time.sleep(0.1)
                record.update({abcd+'X': a_r(0), abcd+'Y': a_r(1), abcd+'Z': a_r(2)})
            print record
            print tableSlot
            table_service.insert_or_replace_entity(getMLTableName(), 'NEUTRAL', tableSlot, record)
    elif x == 's':
        print 'In 5 seconds start shaking'
        print 'send 1000 points of data to ML set marked shaking'
        time.sleep(5.0)
        print 'START'
        time.sleep(0.5)
        for tableSlot in TableSlotShaking:
            for abcd in periods:
                time.sleep(0.1)
                record.update({abcd+'X': a_r(0), abcd+'Y': a_r(1), abcd+'Z': a_r(2)})
            print record
            print tableSlot
            table_service.insert_or_replace_entity(getMLTableName(), 'SHAKING', tableSlot, record)
    elif x == 'sp':
        print 'In 5 seconds start spinning'
        print 'send 1000 points of data to ML set marked spinning'
        time.sleep(5.0)
        print 'START'
        time.sleep(0.5)
        for tableSlot in TableSlotSpinning:
            for abcd in periods:
                time.sleep(0.1)
                record.update({abcd+'X': a_r(0), abcd+'Y': a_r(1), abcd+'Z': a_r(2)})
            print record
            print tableSlot
            table_service.insert_or_replace_entity(getMLTableName(), 'SPINNING', tableSlot, record)
    elif x == 'p':
        print 'In 5 seconds start punching'
        print 'send 1000 points of data to ML set marked punching'
        time.sleep(5.0)
        print 'START'
        time.sleep(0.5)
        for tableSlot in TableSlotPunching:
            for abcd in periods:
                time.sleep(0.1)
                record.update({abcd+'X': a_r(0), abcd+'Y': a_r(1), abcd+'Z': a_r(2)})
            print record
            print tableSlot
            table_service.insert_or_replace_entity(getMLTableName(), 'PUNCHING', tableSlot, record)
    elif x == 'h':
        print 'In 5 seconds start hugging'
        print 'send 1000 points of data to ML set marked hugging'
        time.sleep(5.0)
        print 'START'
        time.sleep(0.5)
        for tableSlot in TableSlotHugging:
            for abcd in periods:
                time.sleep(0.1)
                record.update({abcd+'X': a_r(0), abcd+'Y': a_r(1), abcd+'Z': a_r(2)})
            print record
            print tableSlot
            table_service.insert_or_replace_entity(getMLTableName(), 'HUGGING', tableSlot, record)
    elif x == 't':
        print 'In 5 seconds start throwing'
        print 'send 1000 points of data to ML set marked throwing'
        time.sleep(5.0)
        print 'START'
        time.sleep(0.5)
        for tableSlot in TableSlotThrowing:
            for abcd in periods:
                time.sleep(0.1)
                record.update({abcd+'X': a_r(0), abcd+'Y': a_r(1), abcd+'Z': a_r(2)})
            print record
            print tableSlot
            table_service.insert_or_replace_entity(getMLTableName(), 'THROWING', tableSlot, record)
    