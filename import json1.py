import json
def mydata():
    userdata='{"username":"anu","password":"123","designation":"manager"}'
    dataobj=json.loads(userdata)
    print(dataobj["username"])
    print(dataobj["password"])
mydata()