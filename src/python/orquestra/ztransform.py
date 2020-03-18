"""
This module saves a welcome message.
"""

import json

def ztransform(message):
    zessage = []

    for word in message.split():
        l = list(word)
        l[0] = "Z"
        zessage.append(''.join(l))

    zessage_str = ' '.join(zessage)

    with open("z_message.json",'w') as f:
      f.write(json.dumps(zessage_str, indent=2)) # Write message to file as this will serve as output artifact