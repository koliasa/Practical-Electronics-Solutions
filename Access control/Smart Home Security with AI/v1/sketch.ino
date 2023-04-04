#include <Servo.h>
#include <SoftwareSerial.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>
#include <UbidotsMicroESP8266.h>
#include <WiFiManager.h>
#include <Face.h>
#include <OV7670.h>

#define SSID "your_wifi_ssid"
#define PASSWORD "your_wifi_password"
#define SERVER "http://your_server_url.com"

#define LED_PIN 13
#define SERVO_PIN 3
#define LCD_ADDRESS 0x27
#define LCD_COLS 16
#define LCD_ROWS 2

#define FACE_WIDTH 92
#define FACE_HEIGHT 112
#define FACE_INTERVAL 5

#define FACE_DATA_SIZE (FACE_WIDTH * FACE_HEIGHT)

OV7670 camera;
FaceRecognizer recognizer;

LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLS, LCD_ROWS);
Servo servo;
WiFiClient client;
Ubidots clientUbidots("your_ubidots_token");

char faceData[FACE_DATA_SIZE];
String faceId;
String recognizedName;

void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  pinMode(LED_PIN, OUTPUT);
  pinMode(SERVO_PIN, OUTPUT);
  servo.attach(SERVO_PIN);
  recognizer.train();
  camera.init();
  camera.setResolution(OV7670::RESOLUTION_QVGA);
  connectWiFi();
}

void loop() {
  camera.startCapture();
  camera.readFrame(faceData, FACE_DATA_SIZE);
  camera.stopCapture();
  if (recognizer.recognize(faceData, faceId)) {
    digitalWrite(LED_PIN, HIGH);
    recognizedName = getPersonName(faceId);
    unlockDoor();
    displayPersonName(recognizedName);
  } else {
    digitalWrite(LED_PIN, LOW);
    sendAlert();
  }
  delay(FACE_INTERVAL);
}

void connectWiFi() {
  WiFiManager wifiManager;
  wifiManager.autoConnect();
}

void unlockDoor() {
  servo.write(90);
  delay(1000);
  servo.write(0);
}

void displayPersonName(String name) {
  lcd.clear();
  lcd.print("Welcome home,");
  lcd.setCursor(0, 1);
  lcd.print(name);
}

void sendAlert() {
  DynamicJsonDocument doc(1024);
  doc["message"] = "Unauthorized access detected";
  doc["timestamp"] = millis();
  serializeJson(doc, Serial);
  HTTPClient http;
  http.begin(client, SERVER);
  http.addHeader("Content-Type", "application/json");
  int httpResponseCode = http.POST(doc);
  http.end();
}

String getPersonName(String id) {
  if (id == "1") {
    return "John";
  } else if (id == "2") {
    return "Mary";
  } else if (id == "3") {
    return "Tom";
  } else {
    return "Unknown";
  }
}
