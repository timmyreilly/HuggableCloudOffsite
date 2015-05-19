#get all the good stuff going

from tokens import *
from azure.storage import TableService, Entity, QueueService
import random
import json
import urllib2

myaccount = getAccount()
mykey = getKey()

table_service = TableService(account_name=myaccount, account_key=mykey)
queue_service = QueueService(account_name=myaccount, account_key=mykey)

queueName = 'acceldata'
tableName = 'accel4'
mlTableName = 'MLTraining'

def getAzureTable():
    '''returns table_service object of current storage account in use'''
    return table_service

def getTableName():
    '''get string of current working table'''
    return tableName

def getMLTableName():
    '''get mlTableName of current working table'''
    return mlTableName

def getAzureQueue():
    '''returns QueueService object of current storage account in use'''
    return queue_service 

def getQueueName():
    '''returns string of current working queue'''
    return queueName

def peekMessageAvailable():
    ''' returns a True is a messsage is available in Queue, False if empty '''
    messages = queue_service.peek_messages(getQueueName())
    for message in messages:
        if message.message_text:
            return True
        else:
            return False

def getMessage():
    ''' returns a unicode string object of the contents of the queue '''
    messages = queue_service.get_messages(getQueueName())
    for message in messages:
        messageText = message.message_text
        queue_service.delete_message(getQueueName(), message.message_id, message.pop_receipt)
        return messageText

def getDictFromQueue():
    ''' returns dictionary of message from Queue ''' 
    if peekMessageAvailable():
        x = eval(getMessage())
        return x
    else:
        return {''}


def generateRandom(xyorz):
    ''' generates random numbers for x (single digit), y(2 digit, z(3 digit) '''
    if xyorz == 'x':
        return random.randint(0, 9)
    if xyorz == 'y':
        return random.randint(10, 99)
    if xyorz == 'z':
        return random.randint(100, 999)

def getQueueCount():
    queue_metadata = queue_service.get_queue_metadata(getQueueName())
    return queue_metadata['x-ms-approximate-messages-count']


def get_input_type():
    'returns n or s and nothing else - TODO: still having issues with returning none'
    state = raw_input("Enter 'n' for neutral or 's' for shaking -> ")
    if state != 'n' and state != 's' :
        print "Invalid input. Try Again "
        get_input_type()
    else:
        return state


def swap(a,b):
    'returns the two items in reverse order'
    return b, a


def return_list_generator(first, last):
    'returns a generator with the first value iterating to the last value for use with ints'
    if first > last:
        first, last = swap(first, last)
    num = first
    while num <= last:
        yield num
        num += 1


def return_states_from_request(result):
    ''' pulls out state from result'''
    x = eval(result)
    first = x['Results']['output1']['value']['Values'][0][13]
    second = x['Results']['output1']['value']['Values'][1][13]
    return first, second

def make_data(one, two):
    '''Returns data object to be passed as JSON'''
    data =  {
     "Inputs": {
         "input1": {
             "ColumnNames": ["PartitionKey", "RowKey", "aX", "aY", "aZ", "bX", "bY", "bZ", "cX", "cY", "cZ", "dX", "dY", "dZ"],
             "Values": [ one, two, ]
             },
         },
     "GlobalParameters": {}
     }
    return data

def make_list_from_dict(x):
    l = ['value', '']
    y = sorted(x)
    for i in y:
        l.append(x[i])
    l = map(str, l)
    return l

    #if x[0] == '':
    #    return l
    #else:
    #    y = sorted(x)
    #    for i in y:
    #        l.append(x[i])
    #    l = map(str, l)
    #    return l
    

def make_list_from_dict_v(x):
    l = ['value', '']
    y = sorted(x)
    try:
        for i in y:
            l.append(x[i])
        l = map(str, l)
    except TypeError:
        print ('error of type: TypeError')
        return l
           


def get_result_from_ml(data):
    '''Pass data dict to this function and receive the response from ML'''
    body = str.encode(json.dumps(data))
    url = get_ml_url()
    api_key = getMLAPIKey()
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib2.Request(url, body, headers)

    try:
        response = urllib2.urlopen(req)

        result = response.read()
        return result
    except urllib2.HTTPError, error:
        print("The request failed with status code: " + str(error.code))
        print(error.info())
        print(json.loads(error.read()))

def get_two_states():
    '''returns tuple of next two states from Queue'''
    gd = getDictFromQueue
    makel = make_list_from_dict
    md = make_data
    getr = get_result_from_ml
    rs = return_states_from_request

    return rs(getr(md(makel(gd()), makel(gd()))))

def delete_queue():
    ''' deletes current queue name '''
    queue = getAzureQueue()
    queue.delete_queue(getQueueName())

def set_new_queue_name(newName):
    ''' 
    allows creation of new Queue
    call getQueueName again with createNewQueue to begin using a new queue 
    '''
    queueName = newName

def create_new_queue():
    ''' creates a queue of the string stored in queueName '''
    queue = getAzureQueue()
    queue.create_queue(getQueueName())


def clear_queue():
    ''' 
    Clears out all message from the Queue, to be used when we need to start fresh
    or when we need to catch up.  
    '''
    queue = getAzureQueue()
    queue.clear_messages(getQueueName())


def peek_message():
    messages = queue_service.peek_messages(getQueueName())
    for message in messages:
        print(message.message_text)


def is_queue_over_ten():
    if eval(getQueueCount()) > 10:
        return True
    else:
        return False

 
def process_messages_from_queue():
    ''' 
    returns tuple of two next messages
    and manages the queue length if too long
    and returns false if nothing available
    '''
    qCount = eval(getQueueCount())
    gd = getDictFromQueue
    makel = make_list_from_dict
    md = make_data
    getr = get_result_from_ml
    rs = return_states_from_request
    print qCount
    if qCount <= 0:
        print 'Queue Empty'
        return False
    else:
        l = makel(gd())
        r = rs(getr(md(l, l)))
        if qCount > 10:
            print 'Queue too large -- clearing'
            clear_queue()
            print r
            return r
        else:
            print 'Queue just right'
            print r
            return r


    #x = getDictFromQueue()
    #l = make_list_from_dict(x)
    #d = make_data(l, l)
    
    #r = get_result_from_ml(d)
    #s = return_states_from_request(r)
    #return s

#data =  {
#     "Inputs": {
#         "input1": {
#             "ColumnNames": ["PartitionKey", "RowKey", "aX", "aY", "aZ", "bX", "bY", "bZ", "cX", "cY", "cZ", "dX", "dY", "dZ"],
#             "Values": [ [ "value", "", "123", "191", "1015", "30", "101", "1015", "19", "73", "1014", "31", "64", "1013" ], [ "value", "", "277", "239", "992", "428", "381", "992", "423", "359", "993", "423", "349", "993" ], ]
#             },
#         },
#     "GlobalParameters": {}
#     }