import json
def allIdUsed():
    with open("masterIds.json", "r") as f:
        data = json.loads(f.read())
        data = list(data.values())
    with open("usedIds.json", "w") as f:
        f.write(json.dumps(data))
allIdUsed()
