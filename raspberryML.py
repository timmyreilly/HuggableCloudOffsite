import time

from helperFUNctions import *

from azure.storage import Entity, QueueService

import spidev 

spi = spidev.SpiDev()
spi.open(0,0)

myaccount = getAccount()
mykey + 