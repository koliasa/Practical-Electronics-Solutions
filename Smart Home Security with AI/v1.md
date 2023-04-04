# Arduino Smart Home Security

This repository contains an example of using an Arduino board with an OV7670 camera and a Face Recognition library to build a smart home security system that can recognize authorized individuals and unlock the door for them.

## Hardware requirements

- Arduino board (tested on Uno and Nano)
- OV7670 camera module
- Servo motor
- 16x2 LCD display with I2C adapter
- LED
- Jumper wires
- Breadboard

## Software requirements

- Arduino IDE
- ESP8266WiFi library
- ESP8266HTTPClient library
- ArduinoJson library
- UbidotsMicroESP8266 library
- WiFiManager library
- Face library
- OV7670 library
- LiquidCrystal_I2C library
- A Ubidots account and API token
- A WiFi network

## Installation

1. Install the required libraries in the Arduino IDE.
2. Connect the hardware components according to the wiring diagram in the `wiring_diagram.png` file.
3. Update the `SSID`, `PASSWORD`, and `SERVER` constants in the code to match your WiFi network credentials and server URL.
4. Update the `getPersonName()` function to return the names of the authorized individuals and their corresponding face IDs.
5. Upload the code to the Arduino board.

## Usage

1. Power on the Arduino board and wait for it to connect to the WiFi network.
2. Stand in front of the camera and wait for the system to recognize your face.
3. If your face is recognized as authorized, the LED will light up and the servo will unlock the door for a few seconds.
4. If your face is not recognized or is not authorized, an alert will be sent to the specified server.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This project was inspired by the work of Adafruit and OpenCV. Thank you for your contributions to the maker community.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
If you have any questions or comments about this project, please feel free to reach out to us at ihor@koliasa.com.
