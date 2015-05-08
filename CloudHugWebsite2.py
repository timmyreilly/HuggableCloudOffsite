import time

from tokens import *
from helperFUNctions import *

from flask import Flask, render_template
app = Flask(__name__)




while True:
    if peekMessageAvailable():
        x = eval(getMessage())
        for i in sorted(x):
            print str(i) + ' ' + str(x[i])
    else:
        x = 'Nothing in Queue'



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