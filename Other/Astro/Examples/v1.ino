#include <Wire.h>
#include <RTClib.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <WiFiUdp.h>
#include <TimeLib.h>
#include <Timezone.h>
#include <OpenWeatherMapCurrent.h>

// WiFi settings
const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";

// OpenWeatherMap settings
const char* apiKey = "your_API_KEY";
const char* city = "Kyiv";
const char* countryCode = "ua";

// RTC settings
RTC_DS3231 rtc;

// Timezone settings
TimeChangeRule dstStart = {"DST", Last, Sun, Mar, 3, 60};
TimeChangeRule dstEnd = {"STD", Last, Sun, Oct, 4, 0};
Timezone myTZ(dstStart, dstEnd);

// Relay pin
const int relayPin = 2;

void setup() {
  Serial.begin(115200);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("connected!");

  // Initialize RTC
  Wire.begin();
  rtc.begin();
  if (!rtc.isrunning()) {
    Serial.println("RTC is NOT running!");
  }
  
  // Set sync provider and interval for NTP time
  setSyncProvider(getNtpTime);
  setSyncInterval(ntpSyncInterval);

  // Initialize relay pin
  pinMode(relayPin, OUTPUT);
}

void loop() {
  // Get the current time
  time_t t = myTZ.toLocal(now());
  DateTime nowDT = rtc.now();
  
  // Get weather data
  OpenWeatherMapCurrentData data;
  if (getWeatherData(apiKey, city, countryCode, data)) {
    // Get sunrise and sunset times
    time_t sunrise = myTZ.toUTC(localSunrise(nowDT, data.city.lat, data.city.lon));
    time_t sunset = myTZ.toUTC(localSunset(nowDT, data.city.lat, data.city.lon));
    
    // Turn on the relay if it's after sunset but before sunrise
    if (t >= sunrise && t < sunset) {
      digitalWrite(relayPin, LOW);
    } else {
      digitalWrite(relayPin, HIGH);
    }
  }
  
  // Print current time
  Serial.print("Current time: ");
  Serial.println(formatDateTime(t));
  
  // Wait for a few seconds
  delay(5000);
}

// Get NTP time
time_t getNtpTime() {
  const char* ntpServer = "pool.ntp.org";
  const int timeZone = 2;
  const int ntpPacketSize = 48;

  byte packetBuffer[ntpPacketSize];
  memset(packetBuffer, 0, ntpPacketSize);
  packetBuffer[0] = 0b11100011;
  packetBuffer[1] = 0;
  packetBuffer[2] = 6;
  packetBuffer[3] = 0xEC;
  packetBuffer[12] = 49;
  packetBuffer[13] = 0x4E;
  packetBuffer[14] = 49;
  packetBuffer[15] = 52;

  IPAddress serverIP;
  WiFi.hostByName(ntpServer, serverIP);
  
  WiFiUDP udp;
  udp.begin(123);
  udp.beginPacket(serverIP, 123);
  udp.write(packetBuffer, ntpPacketSize);
  udp.endPacket();

  byte buffer[ntpPacketSize];
