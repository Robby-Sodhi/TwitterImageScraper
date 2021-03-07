import os.path
from os import path
from exceptions import FileError
import json
masterIdList = "masterIds.json"

def checkFile(file):
    if ((not (path.exists(file)))):
        raise FileError(file)


def readMasterId():
    checkFile(masterIdList)
    with open(masterIdList, "r") as f:
        data = json.loads(f.read())
    return data

def isMasterIdEmpty():
    data = readMasterId()
    if len(data) < 0:
        return True

def writeMasterIds(data):
    checkFile(masterIdList)
    with open(masterIdList, "w") as f:
        f.write(json.dumps(data))
