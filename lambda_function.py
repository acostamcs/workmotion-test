import json

def lambda_handler(event, context):
    
    response = f"\nWelcome to our demo API, here are the details of your request: \nHeaders: Content-Type: application/json \nMethod: Get Body: 'username':{event['username']}, 'password':{event['password']}"
    
    return {"headers":{"Content-Type": "application/json"} , "body":json.dumps(response)}
    
    
