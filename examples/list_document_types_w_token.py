from PPPForgivenessSDK.client import Client

# to run file 'list_dcument_types.py', use valid token (page parameter can be changed )
client = Client(access_token='9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b',   environment='sandbox')

document_type_api = client.document_types

# read first page of document types
result = document_type_api.list(page=1)

if result['status'] == 200:
    print(result['data'])
else:
    print("An error occurred." + str(result['status']))
    print(result['data'])

