import urllib2
# If you are using Python 3+, import urllib instead of urllib2

import json 
from helperFUNctions import *


data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["PartitionKey", "RowKey", "aX", "aY", "aZ", "bX", "bY", "bZ", "cX", "cY", "cZ", "dX", "dY", "dZ"],
                    "Values": [ [ "value", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0" ], [ "value", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0" ], ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/e793c9836a854f95a5a795338e41f45b/services/99f8020f388544928e0305d61e7a7043/execute?api-version=2.0&details=true'
api_key = getMLAPIKey()
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers) 

try:
    response = urllib2.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = response.read()
    print(result) 
except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))  