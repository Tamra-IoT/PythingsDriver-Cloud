# PythingsDriver-Cloud
## Drive multiple nodes with a single Python script

PythingsDriver-Cloud is a Python package that allows you to remotely manage, control, and monitor your Tamra boards. PythingsDriver uses similar syntaxes used in the Arduino library to make it easy for those who know how to build a code on a single board, like Arduino UNO. Here, using PythingsDriver, you can deploy and manage a group of Tamra boards using a single script.

## Getting Started
PythingsDriver basically defines tamra_node class
- First you need to create a tamra node object. here the line below creates node1 as an tamra object
#### 1. Creating tamra node object

```py
node1 = tamra_node(env)
```
env is python dictionary has all required configuration to hock with tamra MQTT broker and backend

#### 2. Connecting to tamra broker

```py
node1.connect_tamra_broker()
```
#### 3. Reading Analog/Digital pin
like in the Arduino analogRead(pin) and digitalRead(pin) here PythingsDriver has a similar syntax but you need to add object name before it, as you may have multiple nodes collborate to execute your logic. The Example below uses node1 as the tamra_node object

```py
# read analog pin A0 and save value at A0_reading
A0_reading = node1.analogRead(A0)
```

```py
# read digital pin D5 and save value at D5_reading
D5_reading = node1.digitalRead(D5)
```

#### 4. Writing a value on Analog/Digital pin
like in the Arduino analogWrite(pin,value) and digitalwrite(pin,value) here PythingsDriver has a similar syntax but you need to add object name before it, as you may have multiple nodes collborate to execute your logic. The Example below uses node1 as the tamra_node object

```py
# write 200 on pin D3 (D3 is defined as PWM and here this line set its value to be 200)
node1.analogwrite(D3,200)
```

```py
# write 1 on digital pin D5
node1.digitalwrite(D5,1)
```
