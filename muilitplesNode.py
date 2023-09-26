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
env_path1 = os.path.join(os.path.dirname(__file__), '.env_node1')
# Read the .env file and collect its attributes 
env_vars = env.read_env_file(env_path1)
node1=tamra_node(env_vars)
node1.connect_tamra_broker()

# Define the path to the .env file (assuming it is in the same directory as this script)
env_path2 = os.path.join(os.path.dirname(__file__), '.env_node2')
# Read the .env file and collect its attributes 
env_vars = env.read_env_file(env_path2)
node2=tamra_node(env_vars)
node2.connect_tamra_broker()

pygame.time.wait(2000)

while True:
    node1.digitalWrite(D13,1)
    node2.digitalWrite(D13,0)
    pygame.time.wait(3000)
    node1.digitalWrite(D13,0)
    node2.digitalWrite(D13,1)
    pygame.time.wait(3000)
    switch =node1.digitalRead(D2)
    print(f"switch = {switch}")
    if switch == 1:
        node2.digitalWrite(D3,1)
    else:
        node2.digitalWrite(D3,0)
    pygame.time.wait(2000)
    

