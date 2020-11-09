
from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

greeting_schema = {
    'type': 'object',
    'properties': {
        'date_first': {
            'type': 'string'
        },
        'date_second': {
            'type': 'string'
        },
        'channel': {
            'type': 'string'
        },
        # 'frame': [
        #     {
        #         'time': 'string',
        #         'tvshow_num': 'string',
        #         'cha_num': 'integer'
        #     }
        # ]
    },

    'required': ['date_first']
}


class GreetingInputs(Inputs):
    json = [JsonSchema(schema=greeting_schema)]


def validate_greeting(request):
    inputs = GreetingInputs(request)
    if inputs.validate():
        return None
    else:
        return inputs.errors
