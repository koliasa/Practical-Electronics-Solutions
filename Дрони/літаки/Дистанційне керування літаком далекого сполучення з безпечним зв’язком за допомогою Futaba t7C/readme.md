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

