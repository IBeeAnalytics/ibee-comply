def lambda_handler(event, context):
    message = "this is network engine"
    print(message)
    return {
        "statusCode": 200,
        "body": message
    }
