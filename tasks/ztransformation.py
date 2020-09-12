import json
from orquestra import ztransform

def z_transformation(message)
    with open(message, 'r') as f:
        message = json.load(f)
    ztransform(message)