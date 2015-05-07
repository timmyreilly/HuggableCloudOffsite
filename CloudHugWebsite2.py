import time

from tokens import *
from helperFUNctions import *

from flask import Flask, render_template
app = Flask(__name__)

#from azure.storage import TableService, Entity, QueueService

#myaccount = getAccount()
#mykey = getKey()

#table_service = TableService(account_name=myaccount, account_key=mykey)
#queue_service = QueueService(account_name=myaccount, account_key=mykey)


        


while True:
    x = eval(getMessage())
    print x
    z = getDictOfUnicode(x)
    print z.get('cZ')

#@app.route("/")
#def home():
#    print 'here'
#    return render_template('base.html')  

#@app.route("/")
#def hello():
#    print getMessage() 
#    return str(getMessage())



if __name__ == "__main__":
    app.run()