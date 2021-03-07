import json
from fileStuff import checkFile, readMasterId

usedIdMasterList = "usedIds.json"



def readUsedIdMasterList():
    checkFile(usedIdMasterList)
    with open(usedIdMasterList, "r") as f:
        data = json.loads(f.read())
        return data
def isIdUsed(id):
        usedIds = readUsedIdMasterList()
        if id in usedIds:
            return True
        return False
def isAllUsed():
    usedIds = readUsedIdMasterList()
    masterIdList = readMasterId()
    if set(masterIdList.values()).issubset(set(usedIds)):
        return True
    return False
def appendId(id):
    data = readUsedIdMasterList()
    data.append(id)
    with open(usedIdMasterList, "w") as f:
        f.write(json.dumps(data))
