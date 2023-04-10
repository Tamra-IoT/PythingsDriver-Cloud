# debug_enabled = True  # Set to False to disable debugging messages
from config import debug_enabled
import paho.mqtt.client as mqtt
import json
import time
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
        self.preparecommands_frame=json.dumps({})
        self.state_frame=json.dumps({})
        self.client = mqtt.Client()
        self.getCommands=False
        self.getOutputs=False
       
        # Topics=['inputs','outputs','settings', 'commands','state']

    def on_subscribe(self,client, userdata, mid, granted_qos):
        print("-")

    def on_message(self,client, userdata, msg):
        message=str(msg.payload)
        begin = message.find("{")
        end = message.rfind("}")
        message_json=json.loads(message[begin:end+1]) 
        print(message_json)
        # print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    
        if str(msg.topic) == self.inputs:
            self.inputs_frame=message_json
        elif msg.topic == self.outputs:
            self.outputs_frame=message_json
            self.getOutputs=True
        elif msg.topic == self.commands:
            self.commands_frame= message_json
            self.getCommands=True
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
    def analogWrite(self,pin,value):
        JSON_frame= self.outputs_frame
        print(JSON_frame)
        if pin in JSON_frame:
            print("Key "+pin+" is present in the dictionary")
            command_frame='{"out":{}}'
            frame=json.loads(command_frame)
            frame["out"][pin]=value
            print(frame)
            self.client.publish(self.commands, json.dumps(frame) , qos=1)
            while not self.getOutputs:
                pass
            self.getOutputs=False


        else:
            print(f"Key {pin} is not defined as a PWM pin")


    def digitalWrite(self,pin,value):
        JSON_frame= self.outputs_frame
        print(JSON_frame)
        if pin in JSON_frame:
            command_frame='{"out":{}}'
            frame=json.loads(command_frame)
            frame["out"][pin]=value
            print(frame)
            while not self.getOutputs:
                self.client.publish(self.commands, json.dumps(frame) , qos=1)
                start_time = time.time()   
                duration =3
                while (time.time() - start_time) < duration:
                    pass
            self.getOutputs=False
        else:
            print(f"Key {pin} is not defined as a digital output")
            # return NULL

    def prepare_digitalWrite(self,pin,value):
            JSON_frame= self.outputs_frame
            frame = json.loads(self.preparecommands_frame)
            print(JSON_frame)
            if pin in JSON_frame:
                frame[pin]=value
                self.preparecommands_frame=json.dumps(frame)
            else:
                print(f"Key {pin} is not defined as a digital output")
                # return NULL
    def sendCommandsFrame(self): 
        command_frame='{"out":{}}'
        frame=json.loads(command_frame)
        frame["out"]=json.loads(self.preparecommands_frame) 
        print(frame) 
        while not self.getOutputs:
            self.client.publish(self.commands, json.dumps(frame) , qos=1)
        ###timer
            start_time = time.time()   
            duration =3
            while (time.time() - start_time) < duration:
                pass
        self.getOutputs=False
        



    def digitalRead(self,pin):
        JSON_frame= self.inputs_frame
        print(JSON_frame)
        if pin in JSON_frame:
            return JSON_frame[pin]
        else:
            print(f"Key {pin} is not defined as a digital output")
    
    def analogRead(self,pin):
        JSON_frame= self.inputs_frame
        # print(JSON_frame)
        if pin in JSON_frame:
            return JSON_frame[pin]
        else:
            print(f"Key {pin} is not define as an analog")

    def pinMode(self, pin, mode, interval=60):
        if interval < 3:
            interval = 3
        JSON_frame= self.settings_frame
        if pin in JSON_frame:
            JSON_frame[pin]["mode"]=mode
            JSON_frame[pin]["int"]=interval
        else:
            print(f"{pin} is not available  in this board")
    
    def install_settings(self):
        JSON_frame= self.settings_frame
        JSON_frame["_applied"]=0
        self.client.publish(self.settings, json.dumps(JSON_frame) , qos=1)

