from PythingsDriver import tamra_node
# import read_env_file
import env
import time
import pygame
from ArduinoUNO import *
import os
# print(read_env_file.env_vars)
motion_detector=A0

# Define the path to the .env file (assuming it is in the same directory as this script)
env_path = os.path.join(os.path.dirname(__file__), '.env')

# Read the .env file and collect its attributes 
env_vars = env.read_env_file(env_path)

smart_home=tamra_node(env_vars)
smart_home.connect_tamra_broker()
# print("smart_home.settings_frame")
# print(smart_home.settings_frame)
# Pause for 2 seconds
pygame.time.wait(2000)
# print(smart_home.settings_frame)

while True:
    smart_home.prepare_digitalWrite(D3,1)
    smart_home.prepare_digitalWrite(D5,255)
    smart_home.prepare_digitalWrite(D6,255)
    smart_home.prepare_digitalWrite(D9,1)
    smart_home.prepare_digitalWrite(D11,255)
    # smart_home.prepare_digitalWrite(D10,1)
    # smart_home.prepare_digitalWrite(D12,1)
    # smart_home.prepare_digitalWrite(D13,1)
    smart_home.sendCommandsFrame()
    pygame.time.wait(3000)
    smart_home.prepare_digitalWrite(D3,0)
    smart_home.prepare_digitalWrite(D5,0)
    smart_home.prepare_digitalWrite(D6,0)
    smart_home.prepare_digitalWrite(D9,0)
    smart_home.prepare_digitalWrite(D11,0)
    # smart_home.prepare_digitalWrite(D10,0)
    # smart_home.prepare_digitalWrite(D12,0)
    # smart_home.prepare_digitalWrite(D13,0)
    smart_home.sendCommandsFrame()
    pygame.time.wait(3000)
    

# smart_home.pinMode(D9, OUTPUT)
# smart_home.pinMode(D5, PWM,5)
# smart_home.pinMode(A0, ANALOG,5)
# smart_home.install_settings()
# time.sleep(10)
# print(smart_home.settings_frame)
# time.sleep(2)
# smart_home.digitalWrite(A2,1)
# # time.sleep(5)
# # Pause for 2 seconds
# pygame.time.wait(2000)
# smart_home.digitalWrite(A2,0)
# time.sleep(2)
# smart_home.digitalWrite(D3,0)
# time.sleep(2)
# smart_home.digitalWrite(D10,0)
# time.sleep(2)
# D8_value=smart_home.digitalRead(D8)
# time.sleep(2)
# D9_value=smart_home.analogRead(A0)
# time.sleep(2)
# smart_home.analogWrite(D5,200)
# time.sleep(2)
# smart_home.analogWrite(D3,200)
# time.sleep(2)
# smart_home.analogWrite(A1,200)
# time.sleep(2)
# smart_home.analogWrite(D7,200)
# time.sleep(2)
# print(f"D8_value {D8_value}")
# time.sleep(2)
# print(f"D9_value {D9_value}")
# time.sleep(2)


# while(1):
#     time.sleep(5)
#     print(smart_home.settings_frame)
   
    # smart_home.digitalWrite(D3,1)
    # smart_home.digitalWrite(D10,1)
    # time.sleep(2)
    # smart_home.digitalWrite(D3,0)
    # smart_home.digitalWrite(D10,0)
    # D8_value=smart_home.analogRead(A5)
    # D9_value=smart_home.analogRead(A0)
    # smart_home.analogWrite(D5,200)
    # smart_home.analogWrite(D3,200)
    # smart_home.analogWrite(A1,200)
    # smart_home.analogWrite(D7,200)
    # print(f"D8_value {D8_value}")
    # print(f"D9_value {D9_value}")

    # time.sleep(5)
   
    # settings= smart_home.settings_frame
    # print(settings["A0"])
# print(smart_home.settings_frame)    
# print(smart_home.env)
# print(smart_home.BACKEND_URL)
# print(smart_home.MQTT_PORT)
# print(type(smart_home.MQTT_PORT))
# print(smart_home.MQTT_USERNAME)
# print(smart_home.MQTT_PASSWORD)
# print(smart_home.ACTIVATION_CODE)
# print(smart_home.NODE_ID)
# print(smart_home.commands_frame)

