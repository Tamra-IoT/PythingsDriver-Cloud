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
node1=tamra_node(env_vars)
node1.connect_tamra_broker()

pygame.time.wait(2000)

while True:
    node1.prepare_digitalWrite(D13,1)
    node1.sendCommandsFrame()
    pygame.time.wait(3000)
    node1.prepare_digitalWrite(D13,0)
    node1.sendCommandsFrame()
    pygame.time.wait(3000)
    

