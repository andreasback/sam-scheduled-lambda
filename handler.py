import json

def handler(event, context):
    print "Scheduled Lambda Function"
    print json.dumps(event, indent=4)

    return event