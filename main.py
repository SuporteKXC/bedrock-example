import boto3
import json

def handler(event, context):
    user_input = json.loads(event.body)



    return {
        statusCode: 200,
        body: json.dumps({
            message: 'asxdcasdasdasdasd'
        })
    }
