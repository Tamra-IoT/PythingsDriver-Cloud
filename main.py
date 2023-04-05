# debug_enabled = True  # Set to False to disable debugging messages
from config import debug_enabled
import read_env_file
import paho.mqtt.client as mqtt
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
        # Topics=['inputs','outputs','settings', 'commands','state']

   

    def connect_tamra_broker(self):
        def on_subscribe(client, userdata, mid, granted_qos):
            print("-")

        def on_message(client, userdata, msg):
            message=str(msg.payload)
            begin = message.find("{")
            end = message.rfind("}")
            # NodeFrames[msg.topic]=json.loads(message[begin:end+1])
            print("*"*100)
            print("received")
            print(msg.topic)  
            print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    
            print("*"*100)
            # if str(msg.topic) == self.inputs:
            #     print("catch inputs")
            #     ReceivedFrames["inputs"]=1
            # if msg.topic == self.outputs:
            #     ReceivedFrames["outputs"]=1 
        client = mqtt.Client()
        client.username_pw_set(self.MQTT_USERNAME, self.MQTT_PASSWORD)
        client.on_subscribe = on_subscribe
        client.on_message = on_message
        client.connect(self.MQTT_URL, self.MQTT_PORT)
        client.subscribe(self.settings, qos=1)
        client.subscribe(self.inputs, qos=1)
        client.subscribe(self.outputs, qos=1)
        client.subscribe(self.commands, qos=1)
        client.loop_start()

        


    def say_hello(self):
        print(f"Hello, {self.name}!")

# print(read_env_file.env_vars)

smart_home=tamra_node(read_env_file.env_vars)
smart_home.connect_tamra_broker()

while(1):
    time.sleep(5)
# print(smart_home.env)
# print(smart_home.BACKEND_URL)
# print(smart_home.MQTT_PORT)
# print(type(smart_home.MQTT_PORT))
# print(smart_home.MQTT_USERNAME)
# print(smart_home.MQTT_PASSWORD)
# print(smart_home.ACTIVATION_CODE)
# print(smart_home.NODE_ID)
# print(smart_home.inputs)