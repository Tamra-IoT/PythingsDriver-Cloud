# PythingsDriver-Cloud
## Drive multiple nodes with a single Python script

PythingsDriver-Cloud is a Python package that allows you to remotely manage, control, and monitor your Tamra boards. PythingsDriver uses similar syntaxes used in the Arduino library to make it easy for those who know how to build a code on a single board, like Arduino UNO. Here, using PythingsDriver, you can deploy and manage a group of Tamra boards using a single script.

## Getting Started
PythingsDriver basically defines tamra_node class
- First you need to create a tamra node object. here thie line below create node1 as an tamra object
1. Creating tamra node object

```py
node1 = tamra_node(env)
```
env is python dictionary has all required configuration to hock with tamra MQTT broker and backend

2. Connecting to tamra broker

```py
node1.connect_tamra_broker()
```
