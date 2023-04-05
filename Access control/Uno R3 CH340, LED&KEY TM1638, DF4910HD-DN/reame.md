## Project Description
This project aims to create an access control system that uses facial recognition as a means of authentication. The system is built using an Arduino Uno R3 CH340, LED&KEY TM1638, 2-channel relay module, and DF4910HD-DN. The software is written in C++ and is compatible with Arduino, PIC, ARM, and AVR platforms. The system includes features such as customizable time settings, delay settings, visitor tracking, and authentication through facial recognition.

## Requirements
- Arduino Uno R3 CH340
- LED&KEY TM1638
- 2-channel relay module 5V for Arduino PIC ARM AVR
- DF4910HD-DN
- Ubuntu 18.04

Code Arduino Uno R3 CH340:
```C++
#include <Wire.h>
#include <Adafruit_MLX90614.h>
#include <Adafruit_SSD1306.h>
#include <SoftwareSerial.h>
#include <Servo.h>
#include <EEPROM.h>
#include <SPI.h>
#include <TM1638.h>
#include <MFRC522.h>
#include <Adafruit_GFX.h>
#include <Adafruit_PCD8544.h>
#include <dlib/dnn.h>
#include <dlib/data_io.h>
#include <dlib/image_processing.h>
#include <dlib/image_processing/frontal_face_detector.h>
#include <dlib/image_processing/render_face_detections.h>
#include <dlib/image_processing.h>
#include <dlib/gui_widgets.h>
#include <dlib/image_io.h>
#include <dlib/opencv.h>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/opencv.hpp>

// Constants
const int SERVO_PIN = 9;
const int GREEN_LED = 10;
const int RED_LED = 11;
const int RELAY_1 = 12;
const int RELAY_2 = 13;
const int EEPROM_SIZE = 512;
const int MAX_VISITORS = 10;
const int MAX_NAME_LENGTH = 30;
const int MAX_ATTEMPTS = 3;
const int FACE_DOWNSAMPLE_RATIO = 2;
const int FACE_FRAME_SKIP = 2;
const int FACE_ROI_SIZE = 150;
const int FACE_THROTTLE_TIME = 3000;

// Global variables
Adafruit_SSD1306 display(128, 32, &Wire, -1);
SoftwareSerial serial(2, 3);
TM1638 tm1638(8, 9, 10);
Servo servo;
MFRC522 mfrc522(4, 5);
Adafruit_PCD8544 lcd = Adafruit_PCD8544(7, 6, 5, 4, 3);

unsigned long last_face_time = 0;

bool is_door_locked = true;
bool is_user_authenticated = false;
bool is_key_pressed = false;

char visitors[MAX_VISITORS][MAX_NAME_LENGTH];
int num_visitors = 0;

int selected_time = 5;
int selected_delay = 5;

// Face detection objects
dlib::frontal_face_detector face_detector = dlib::get_frontal_face_detector();
dlib::shape_predictor landmark_detector;
dlib::matrix<dlib::rgb_pixel> face_chip;

// Helper functions
void displayWelcomeMessage() {
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0, 0);
  display.println("Welcome to the");
  display.println("Access Control System");
  display.display();
}

void displayUserAuthenticated() {
  lcd.clearDisplay();
  lcd.setCursor(0,0);
  lcd.print("Access Granted");
  lcd.setCursor(0,1);
  lcd.print("Welcome, ");
  lcd.print(visitors[num_visitors-1]);
  lcd.display();
}

void displayUserDenied() {
  lcd.clearDisplay();
  lcd.setCursor(0,0);
  lcd.print("Access Denied");
  lcd.display();
}

void displayTimeSettings() {
  tm1638.clearDisplay();
  tm1638.setLED(TM1638_DOT3, true);
  tm1638.setLED(TM1638_DOT4, true);
  tm1638.setDisplayToDecNumber(selected_time, false);
}

void displayDelaySettings() {
  tm1638.clearDisplay();
  tm1638.setLED(TM1638_DOT3, true);
  tm1638.setLED(TM1638_DOT4, true);
  tm1638.setDisplayToDecNumber(selected_delay, false);
}

void unlockDoor() {
  servo.write(0);
  digitalWrite(GREEN_LED, HIGH);
  digitalWrite(RED_LED, LOW);
  digitalWrite(RELAY_1, HIGH);
  digitalWrite(RELAY_2, HIGH);
  is_door_locked = false;
}

void lockDoor() {
  servo.write(90);
  digitalWrite(GREEN_LED, LOW);
  digitalWrite(RED_LED, HIGH);
  digitalWrite(RELAY_1, LOW);
  digitalWrite(RELAY_2, LOW);
  is_door_locked = true;
}

void addVisitor(char name[]) {
  if (num_visitors >= MAX_VISITORS) {
    return;
  }

  strcpy(visitors[num_visitors], name);
  num_visitors++;

  EEPROM.write(0, num_visitors);

  for (int i = 0; i < num_visitors; i++) {
    EEPROM.put(i * MAX_NAME_LENGTH + 1, visitors[i]);
  }

  EEPROM.commit();
}

bool isVisitor(char name[]) {
  for (int i = 0; i < num_visitors; i++) {
    if (strcmp(name, visitors[i]) == 0) {
      return true;
    }
  }

  return false;
}

void deleteVisitor(int index) {
  if (index >= num_visitors) {
    return;
  }

  num_visitors--;

  for (int i = index; i < num_visitors; i++) {
    strcpy(visitors[i], visitors[i+1]);
  }

  EEPROM.write(0, num_visitors);

  for (int i = 0; i < num_visitors; i++) {
    EEPROM.put(i * MAX_NAME_LENGTH + 1, visitors[i]);
  }

  EEPROM.commit();
}

void handleKeypadInput() {
  if (tm1638.getButtons()) {
    int button = tm1638.getButtons();
    is_key_pressed = true;

    if (button == TM1638_BUTTON_LEFT) {
      selected_time--;
      if (selected_time < 1) {
        selected_time = 1;
      }
      displayTimeSettings();
    } else if (button == TM1638_BUTTON_RIGHT) {
      selected_time++;
      if (selected_time > 10) {
        selected_time = 10;
      }
      displayTimeSettings();
    } else if (button == TM1638_BUTTON_OK) {
      selected_delay--;
      if (selected_delay < 1) {
        selected_delay = 1;
      }
      displayDelaySettings();
    } else if (button == TM1638_BUTTON_CANCEL) {
      selected_delay++;
      if (selected_delay > 10) {
        selected_delay = 10;
      }
      displayDelaySettings();
    }
  } else {
    is_key_pressed = false;
  }
}

void handleRFIDInput() {
  if
void handleRFIDInput() {
  if (rfid.isCard()) {
    if (!is_card_detected) {
      is_card_detected = true;

      if (!rfid.readCardSerial()) {
        return;
      }

      char uid[MAX_UID_LENGTH];
      sprintf(uid, "%02X%02X%02X%02X", rfid.serNum[0], rfid.serNum[1], rfid.serNum[2], rfid.serNum[3]);

      if (isVisitor(uid)) {
        displayUserGranted();
        unlockDoor();
        last_unlocked_time = millis();
      } else {
        displayUserDenied();
      }
    }
  } else {
    is_card_detected = false;
  }
}

void setup() {
  Serial.begin(9600);

  lcd.begin(16, 2);
  lcd.clear();
  lcd.display();

  tm1638.init();
  tm1638.clearDisplay();

  pinMode(GREEN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  pinMode(RELAY_1, OUTPUT);
  pinMode(RELAY_2, OUTPUT);
  servo.attach(SERVO_PIN);

  rfid.init();
  SPI.begin();
  rfid.setSPIConfig();
  is_card_detected = false;

  num_visitors = EEPROM.read(0);
  for (int i = 0; i < num_visitors; i++) {
    char name[MAX_NAME_LENGTH];
    EEPROM.get(i * MAX_NAME_LENGTH + 1, name);
    strcpy(visitors[i], name);
  }

  selected_time = EEPROM.read(256);
  if (selected_time == 0xff) {
    selected_time = 5;
  }

  selected_delay = EEPROM.read(257);
  if (selected_delay == 0xff) {
    selected_delay = 5;
  }

  displayTimeSettings();

  lockDoor();
}

void loop() {
  handleKeypadInput();
  handleRFIDInput();

  if (!is_door_locked && (millis() - last_unlocked_time >= selected_time * 1000)) {
    lockDoor();
  }

  if (is_door_locked && !is_key_pressed && (millis() - last_unlocked_time >= selected_delay * 1000)) {
    tm1638.clearDisplay();
    displayTimeSettings();
  }
}
```
## Time Settings
The system allows you to configure the time settings for the access control. There are two settings that you can adjust:
- Access Time: This is the duration of time that the door will remain unlocked after a valid user is detected. By default, it is set to 5 seconds, but you can change it to any value you like.
- Delay Time: This is the duration of time that the system will wait before displaying the time settings again after the door is locked. By default, it is set to 5 seconds, but you can change it to any value you like.

To adjust the time settings, use the keypad to enter the Settings menu, and then select either Access Time or Delay Time. The current value of the setting will be displayed on the TM1638 module. To change the value, use the keypad to enter the new value, and then press the # key to save the new value to EEPROM. The system will then return to the Settings menu.

## Visitor List
The system also allows you to maintain a list of authorized visitors. When a visitor's RFID card is detected, the system will check the card's UID against the list of authorized visitors. If the UID matches an entry in the list, the system will grant access. If not, the system will deny access.

To add a visitor to the list, use the keypad to enter the Settings menu, and then select Add Visitor. The system will prompt you to enter the visitor's name. Use the keypad to enter the name, and then press the # key to save the name to EEPROM. The system will then return to the Settings menu.

To remove a visitor from the list, use the keypad to enter the Settings menu, and then select Remove Visitor. The system will display the list of visitors. Use the keypad to select the visitor you want to remove, and then press the # key to confirm the removal. The system will then return to the Settings menu.