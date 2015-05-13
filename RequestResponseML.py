import urllib2
# If you are using Python 3+, import urllib instead of urllib2
from tokens import *
from helperFUNctions import *
import json 


data =  {
     "Inputs": {
         "input1": {
             "ColumnNames": ["PartitionKey", "RowKey", "aX", "aY", "aZ", "bX", "bY", "bZ", "cX", "cY", "cZ", "dX", "dY", "dZ"],
             "Values": [ [ "value", "", "123", "191", "1015", "30", "101", "1015", "19", "73", "1014", "31", "64", "1013" ], [ "value", "", "277", "239", "992", "428", "381", "992", "423", "359", "993", "423", "349", "993" ], ]
             },
         },
     "GlobalParameters": {}
     }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/e793c9836a854f95a5a795338e41f45b/services/c80158e8638b444eb26d131b2c56e4af/execute?api-version=2.0&details=true'
api_key = getMLAPIKey()
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers) 

try:
    response = urllib2.urlopen(req)

    result = response.read()
    print(result) 
    print (return_states_from_request(result))


except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))    