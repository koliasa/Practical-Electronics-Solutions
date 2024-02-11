**Project Title:** Long-Distance Control of Aircraft using Futaba t7C, NodeMCU Lua ESP8266 CH340, SIM800L, and R617FS

**Description:**
This project aims to implement telemetry using Futaba t7C remote control and NodeMCU Lua ESP8266 CH340 to control the aircraft from a long distance using ardupilot software. The telemetry data will be transmitted over a server-based on Cent os operating system using the protocols lua, Paho MQTT, and AES 256 encryption. Additionally, we will use SIM800L to control the aircraft using SMS commands.

**Hardware Required:**
- Futaba t7C remote control
- NodeMCU Lua ESP8266 CH340
- SIM800L module
- R617FS receiver module
- Aircraft
- Windows-based ground station
- Good Internet channel

**Software Required:**
- Ardupilot software
- CentOS operating system
- Lua
- Paho MQTT
- AES 256 encryption

**Implementation:**
1. Connect the R617FS receiver module to the Futaba t7C remote control and the NodeMCU Lua ESP8266 CH340.
2. Install the SIM800L module on the aircraft and connect it to the NodeMCU Lua ESP8266 CH340.
3. Install the ardupilot software on the NodeMCU Lua ESP8266 CH340 and configure it to receive telemetry data from the aircraft.
4. Install the CentOS operating system on the server and configure it to receive and process the telemetry data transmitted over the internet using Paho MQTT protocol and AES 256 encryption.
5. Use Lua scripting language to code the communication between the NodeMCU Lua ESP8266 CH340 and the server, using Paho MQTT protocol and AES 256 encryption.
6. Use SMS commands via the SIM800L module to control the aircraft remotely.

**Conclusion:**
This project provides a secure and reliable way to control the aircraft from a long distance using Futaba t7C remote control, NodeMCU Lua ESP8266 CH340, SIM800L, and R617FS. The use of ardupilot software, CentOS operating system, Lua scripting language, Paho MQTT protocol, and AES 256 encryption ensures the accuracy, reliability, and security of the telemetry data transmitted over the internet. With the use of SMS commands, the aircraft can be remotely controlled from a distance without the need for a constant internet connection.


# General description of the implementation of this project

1. Hardware Connection
Connect the R617FS receiver module to the Futaba t7C remote control and the NodeMCU Lua ESP8266 CH340. Then, connect the SIM800L module to the NodeMCU Lua ESP8266 CH340.
2. Software Installation
Install the ardupilot software on the NodeMCU Lua ESP8266 CH340 and configure it to receive telemetry data from the aircraft. Then, install the CentOS operating system on the server and configure it to receive and process the telemetry data transmitted over the internet using Paho MQTT protocol and AES 256 encryption.
3. Lua Scripting
Use Lua scripting language to code the communication between the NodeMCU Lua ESP8266 CH340 and the server, using Paho MQTT protocol and AES 256 encryption. You can use the Paho MQTT client library for Lua to send and receive data over MQTT. The AES 256 encryption can be implemented using a Lua encryption library such as LuaCrypto.
4. SMS Control
Use SMS commands via the SIM800L module to control the aircraft remotely. You can use AT commands to send SMS messages to the SIM800L module from your mobile phone or any other device. Then, use Lua scripting on the NodeMCU Lua ESP8266 CH340 to receive and process the SMS commands and control the aircraft accordingly.

### Here is an example Lua script for sending and receiving telemetry data over MQTT
```lua
-- Import required libraries
local mqtt = require("mqtt")
local crypto = require("crypto")

-- Define MQTT broker details
local broker = "192.168.0.10"
local port = 1883
local client_id = "nodeMCU"
local username = "mqtt_username"
local password = "mqtt_password"
local topic = "telemetry"

-- Define AES 256 encryption details
local key = "AES256_KEY"
local iv = "AES256_IV"

-- Define function for encrypting data
function encrypt(data)
  local cipher = crypto.encrypt("AES-256-CBC", key, iv, data)
  return crypto.encode_base64(cipher)
end

-- Define function for decrypting data
function decrypt(data)
  local cipher = crypto.decode_base64(data)
  return crypto.decrypt("AES-256-CBC", key, iv, cipher)
end

-- Define MQTT client and connect to broker
local client = mqtt.client(client_id, 120, username, password)
client:connect(broker, port)

-- Define function for sending telemetry data
function send_telemetry(data)
  -- Encrypt the data
  local encrypted_data = encrypt(data)
  -- Publish the encrypted data to the MQTT broker
  client:publish(topic, encrypted_data, 0, false)
end

-- Define function for receiving telemetry data
function receive_telemetry(data)
  -- Decrypt the data
  local decrypted_data = decrypt(data)
  -- Process the decrypted data
  -- (e.g. control the aircraft, display on a dashboard, etc.)
end

-- Subscribe to the telemetry topic
client:subscribe({[topic]=0})

-- Define callback function for received messages
client:on("message", function(topic, data)
  -- Receive and process the telemetry data
  receive_telemetry(data)
end)

-- Send telemetry data every 5 seconds
tmr.create():alarm(5000, tmr.ALARM_AUTO, function()
  -- Get telemetry data from the ardupilot software
  local telemetry_data = get_telemetry_data()
  -- Send the telemetry data
  send_telemetry(telemetry_data)
end)
```
The code above is just an example and may require modification to fit your specific use
