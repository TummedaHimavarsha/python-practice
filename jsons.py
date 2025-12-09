import json
data=["Tesla","BMW","Fortuner"]
with open("py.json","w") as f:
    json.dump(data,f,indent=4)

import json
dict1={"name":"Himavarsha","age":21}
with open("py.json","w") as f:
    json.dump(dict1,f,indent=4)


import json
with open("py.json","r")as f:
    res=json.load(f)
    print(res,type(res))

import json
with open("py.json","r")as f:
    res=json.load(f)
    res.append("lamborghini")
with open("py.json","w")as f:
    json.dump(res,f,indent=4)



