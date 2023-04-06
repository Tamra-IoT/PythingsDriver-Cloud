# debug_enabled = True  # Set to False to disable debugging messages
from config import debug_enabled
import read_env_file
import paho.mqtt.client as mqtt
import json
import time
from ArduinoUNO import *
class tamra_node:
    def __init__(self, env):
        self.env = env
        self.BACKEND_URL=env["BACKEND_URL"]
        self.MQTT_URL=env["MQTT_URL"]
        self.MQTT_PORT=int(env["MQTT_PORT"])
        self.MQTT_USERNAME=env["MQTT_USERNAME"]
        self.MQTT_PASSWORD=env["MQTT_PASSWORD"]
        self.NODE_ID=env["NODE_ID"]
        self.ACTIVATION_CODE=env["ACTIVATION_CODE"]
        self.preamble=self.ACTIVATION_CODE+'/'+self.NODE_ID+'/'
        self.inputs=self.preamble+'inputs'
        self.outputs=self.preamble+'outputs'
        self.settings=self.preamble+'settings'
        self.commands=self.preamble+'commands'
        self.state=self.preamble+'state'
        self.settings_frame=json.dumps({})
        self.inputs_frame=json.dumps({})
        self.outputs_frame=json.dumps({})
        self.commands_frame=json.dumps({})
        self.state_frame=json.dumps({})
        self.client = mqtt.Client()
       
        # Topics=['inputs','outputs','settings', 'commands','state']

    def on_subscribe(self,client, userdata, mid, granted_qos):
        print("-")

    def on_message(self,client, userdata, msg):
        message=str(msg.payload)
        begin = message.find("{")
        end = message.rfind("}")
        message_json=json.loads(message[begin:end+1]) 
        # print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    
        if str(msg.topic) == self.inputs:
            self.inputs_frame=message_json
        elif msg.topic == self.outputs:
            self.outputs_frame=message_json
        elif msg.topic == self.commands:
            self.commands_frame= message_json
        elif msg.topic == self.state:
            self.state_frame= message_json
        elif msg.topic == self.settings:
            self.settings_frame= message_json


    def connect_tamra_broker(self): 
        self.client.username_pw_set(self.MQTT_USERNAME, self.MQTT_PASSWORD)
        self.client.on_subscribe = self.on_subscribe
        self.client.on_message = self.on_message
        self.client.connect(self.MQTT_URL, self.MQTT_PORT)
        self.client.subscribe(self.settings, qos=1)
        self.client.subscribe(self.inputs, qos=1)
        self.client.subscribe(self.outputs, qos=1)
        self.client.subscribe(self.commands, qos=1)
        self.client.loop_start()

    # def digitalRead(self, pin):

    def digitalWrite(self,pin,value):
        JSON_frame= self.outputs_frame
        print(JSON_frame)
        if pin in JSON_frame:
            print("Key "+pin+" is present in the dictionary")
            command_frame='{"out":{}}'
            frame=json.loads(command_frame)
            frame["out"][pin]=value
            print(frame)

        else:
            print("Key "+pin+" is not present in the dictionary")




    def say_hello(self):
        print(f"Hello, {self.name}!")

# print(read_env_file.env_vars)

smart_home=tamra_node(read_env_file.env_vars)
smart_home.connect_tamra_broker()
print("smart_home.settings_frame")
print(smart_home.settings_frame)

while(1):
    smart_home.digitalWrite(D3,1)
    # print(smart_home.settings_frame)
    time.sleep(5)
   
    settings= smart_home.settings_frame
    # print(settings["A0"])
    
# print(smart_home.env)
# print(smart_home.BACKEND_URL)
# print(smart_home.MQTT_PORT)
# print(type(smart_home.MQTT_PORT))
# print(smart_home.MQTT_USERNAME)
# print(smart_home.MQTT_PASSWORD)
# print(smart_home.ACTIVATION_CODE)
# print(smart_home.NODE_ID)
    print(smart_home.commands_frame)

