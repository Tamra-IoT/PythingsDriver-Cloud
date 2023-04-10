from PythingsDriver import tamra_node
import read_env_file
import time
import pygame
from ArduinoUNO import *
# print(read_env_file.env_vars)
buzzerPort=D3
motion_detector=A0
rain_detector=D7
smoke_sensor=A3 #need to change
RED_LED=D4
motor_door=D11
smart_home=tamra_node(read_env_file.env_vars)
smart_home.connect_tamra_broker()
# print("smart_home.settings_frame")
# print(smart_home.settings_frame)
# Pause for 2 seconds
pygame.time.wait(2000)
# print(smart_home.settings_frame)

while True:
    motion_state=smart_home.analogRead(motion_detector)
    rainy_state=smart_home.analogRead(rain_detector)
    smoke_state=smart_home.analogRead(smoke_sensor)
    power_led=smart_home.outputs_frame[A2]
    door_state=smart_home.outputs_frame[D11]
    RedLED_state=smart_home.outputs_frame[D4]
    buffer_state=smart_home.outputs_frame[buzzerPort]
    # smart_home.prepare_digitalWrite(RED_LED,1)
    #     # pygame.time.wait(1000)
    # smart_home.prepare_digitalWrite(motor_door,80)
    # smart_home.sendCommandsFrame()

    if motion_state>500 and power_led == 0:
        smart_home.digitalWrite(A2,1)
        pygame.time.wait(3000)
    elif motion_state<500 and power_led >= 1:
        smart_home.digitalWrite(A2,0)

    if rainy_state == 1 and RedLED_state == 0:
        smart_home.prepare_digitalWrite(RED_LED,1)
        # pygame.time.wait(1000)
        smart_home.prepare_digitalWrite(motor_door,80)
        smart_home.sendCommandsFrame()
    elif RedLED_state == 1 and rainy_state == 0:
        smart_home.prepare_digitalWrite(RED_LED,0)
        # pygame.time.wait(1000)
        smart_home.prepare_digitalWrite(motor_door,180)
        smart_home.sendCommandsFrame()
    
    if smoke_state < 800 and buffer_state == 0:
        smart_home.digitalWrite(buzzerPort,100)
        pygame.time.wait(3000)
    elif smoke_state > 1000 and buffer_state > 0:
        smart_home.digitalWrite(buzzerPort,0)

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

