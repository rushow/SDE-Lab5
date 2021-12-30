import json
import traceback

def ResponseSuccess(obj):
    return json.dumps({
            'success': True,
            'data': obj
         })

def ResponseFail(message):
    return json.dumps({
            'success': False,
            'message': message,
            'data': None
         })
