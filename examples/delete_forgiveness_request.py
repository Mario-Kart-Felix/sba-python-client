from PPPForgivenessSDK.client import Client

# to run file 'delete_forgiveness_request.py', use valid token and a slug associated with a valid forgiveness request
client = Client(
    access_token='{{YOUR_TOKEN_HERE}}',
    environment='sandbox'
)

forgiveness_api = client.forgiveness_requests

# delete forgiveness request
result = forgiveness_api.delete(slug='{{YOUR_SLUG_HERE}}') # get a single doc type

if result['status'] == 204:
    print(result['data'])
else:
    print("An error occurred." + str(result['status']))
    print(result['data'])