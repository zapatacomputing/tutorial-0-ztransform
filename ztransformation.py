import json

def z_transformation(message):
    with open(message, 'r') as f:
        artifact = json.load(f)

    if "message" not in artifact:
        raise KeyError("Error: Artifact had no 'message' field.")

    z_transform(artifact["message"])

def z_transform(message):
    zessage = []

    for word in message.split():
        l = list(word)
        l[0] = "Z"
        zessage.append(''.join(l))

    zessage_str = ' '.join(zessage)

    zessage_dict = {}
    zessage_dict["message"] = zessage_str
    zessage_dict["schema"] = "message"

    with open("zelcome.json",'w') as f:
      f.write(json.dumps(zessage_dict, indent=2)) # Write message to file as this will serve as output artifact
