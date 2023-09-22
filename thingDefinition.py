json_settings= {
  "D2": {
    "modes": [
      "i",
      "o"
    ],
    "mode": 0,
    "int": 0
  },
  "D3": {
    "modes": [
      "i",
      "o",
      "p"
    ],
    "mode": "p",
    "int": 60
  },
  "D4": {
    "modes": [
      "i",
      "o"
    ],
    "mode": "o",
    "int": 60
  },
  "D5": {
    "modes": [
      "i",
      "o",
      "p"
    ],
    "mode": "p",
    "int": 60
  },
  "D6": {
    "modes": [
      "i",
      "o",
      "p"
    ],
    "mode": "p",
    "int": 60
  },
  "D7": {
    "modes": [
      "i",
      "o"
    ],
    "mode": "i",
    "int": 5
  },
  "D8": {
    "modes": [
      "i",
      "o"
    ],
    "mode": 0,
    "int": 0
  },
  "D9": {
    "modes": [
      "i",
      "o"
    ],
    "mode": "o",
    "int": 60
  },
  "D10": {
    "modes": [
      "i",
      "o"
    ],
    "mode": "o",
    "int": 60
  },
  "D11": {
    "modes": [
      "i",
      "o",
      "p"
    ],
    "mode": "p",
    "int": 60
  },
  "D12": {
    "modes": [
      "i",
      "o"
    ],
    "mode": "o",
    "int": 60
  },
  "D13": {
    "modes": [
      "i",
      "o"
    ],
    "mode": "o",
    "int": 60
  },
  "A0": {
    "modes": [
      "a",
      "i",
      "o"
    ],
    "mode": "a",
    "int": 5
  },
  "A1": {
    "modes": [
      "a",
      "i",
      "o"
    ],
    "mode": "o",
    "int": 60
  },
  "A2": {
    "modes": [
      "a",
      "i",
      "o"
    ],
    "mode": "o",
    "int": 60
  },
  "A3": {
    "modes": [
      "a",
      "i",
      "o"
    ],
    "mode": "a",
    "int": 5
  },
  "A4": {
    "modes": [
      "a",
      "i",
      "o"
    ],
    "mode": 0,
    "int": 0
  },
  "A5": {
    "modes": [
      "a",
      "i",
      "o"
    ],
    "mode": 0,
    "int": 0
  },
  "_applied": 1
}


# print(json_settings)
import json
# thing={}
# thing["name"]="Red LED"
# thing["description"]="this LED can be turned on and turned off"
# print(json.dumps(thing))
# thing["port"]="D2"
# port=thing["port"]
# thing["Port Setting"]=json_settings[port]
# print(json.dumps(thing))

class tamra_thing:
     def __init__(self,name, description,port,node_setting):
        self.jsonFile={}
        self.jsonFile["name"]=name
        self.jsonFile["description"]=description
        self.jsonFile["port"]=port
        self.jsonFile["Port Setting"]={port:node_setting[port]}
        


# thing["name"]="Red LED"
# thing["description"]="this LED can be turned on and turned off"
# print(json.dumps(thing))
# thing["port"]="D2"
# port=thing["port"]
# thing["Port Setting"]=json_settings[port]
# print(json.dumps(thing)
things=[]          
things.append(tamra_thing("Red LED","this LED can be turned on and turned off","D2", json_settings).jsonFile)
things.append(tamra_thing("Red LED","this LED can be turned on and turned off","D2", json_settings).jsonFile)
things.append(tamra_thing("Red LED","this LED can be turned on and turned off","D2", json_settings).jsonFile)

TamraDiscription={}

for i in range(len(things)):
    TamraDiscription[str(i)]=things[i]


print(json.dumps(TamraDiscription))
# print(json.dumps(TamraDiscription))
# for e in TamraDiscription:
#     print(e)