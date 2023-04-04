#!/bin/bash

# Clone required libraries
git clone https://github.com/jbaldwin/libfacedetection.git
git clone https://github.com/adafruit/Adafruit-PWM-Servo-Driver-Library.git
git clone https://github.com/adafruit/Adafruit-GFX-Library.git
git clone https://github.com/fdebrabander/Arduino-LiquidCrystal-I2C-library.git
git clone https://github.com/tzapu/WiFiManager.git
git clone https://github.com/esp8266/Arduino.git esp8266

# Install Ubidots and ArduinoJson libraries
arduino-cli lib install "UbidotsMicroESP8266"
arduino-cli lib install "ArduinoJson"

# Compile and upload sketch
arduino-cli compile -b esp8266:esp8266:nodemcuv2
arduino-cli upload -p /dev/ttyUSB0 -b esp8266:esp8266:nodemcuv2

# Clean up cloned libraries
rm -rf libfacedetection
rm -rf Adafruit-PWM-Servo-Driver-Library
rm -rf Adafruit-GFX-Library
rm -rf Arduino-LiquidCrystal-I2C-library
rm -rf WiFiManager
rm -rf esp8266

## License

This code is licensed under the MIT license. See the [LICENSE](LICENSE) file for details.
