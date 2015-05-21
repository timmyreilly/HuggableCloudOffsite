import time

from tokens import *
from helperFUNctions import *

from flask import Flask, render_template
app = Flask(__name__)


while True:
    m = get_state_managed_queue()
    print m


while True:
    m = process_messages_from_queue()
    print m


while True:
    s = get_two_states()
    if s == False:
        print "Nothing in Queue"
        time.sleep(0.2)
    else:
        print s

    if eval(getQueueCount()) > 5:
        print getQueueCount()
        print 'Clearing Queue'
        clear_queue()




while True:

    x = getDictFromQueue()
    if x == {''}:
        print "Nothing in Queue"
        time.sleep(0.2)
    else:
        for i in sorted(x):
                print str(i) + ' ' + str(x[i])
    


    #x = getDictFromQueue()
    #print x
    #if x:
    #    for i in sorted(x):
    #        print str(i) + ' ' + str(x[i])
    #else: 
    #    print "Queue is empty"


#while True:
#    if getMessage():
#        x = eval(getMessage())
#    else:
#        x = 'nothing to return'
#    print type(x)
#    for i in sorted(x):
#        print str(i) + ' ' + str(x[i])



   
#@app.route("/")
#def home():
#    print 'here'
#    return render_template('base.html')  

#@app.route("/")
#def hello():
#    print getMessage() 
#    return str(getMessage())
#from azure.storage import TableService, Entity, QueueService

#myaccount = getAccount()
#mykey = getKey()

#table_service = TableService(account_name=myaccount, account_key=mykey)
#queue_service = QueueService(account_name=myaccount, account_key=mykey)


        


if __name__ == "__main__":
    app.run()