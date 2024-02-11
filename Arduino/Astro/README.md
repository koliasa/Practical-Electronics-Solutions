# Основна мета проекту

Включати реле при настанні сутінків та вимикати його під час світанку. Для цього будемо використовувати функції, що дозволяють отримувати час, встановлений на модулі RTC, та порівнювати його з часом сходу та заходу сонця в заданому регіоні, також збирати дані з метеостацій для корегування заходу та сходу.

```C++
#include <Wire.h>
#include <RTClib.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <WiFiUdp.h>
#include <TimeLib.h>
#include <Timezone.h>
#include <OpenWeatherMapCurrent.h>

RTC_DS3231 rtc;
WiFiUDP udp;
OpenWeatherMapCurrentData currentWeather;
TimeChangeRule CEST = {"CEST", Last, Sun, Mar, 2, 120};
TimeChangeRule CET = {"CET ", Last, Sun, Oct, 3, 60};
Timezone tz(CEST, CET);

const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";
const char* server = "api.openweathermap.org";
const char* apiKey = "your_API_key";
const float lat = 50.5555;
const float lon = 30.3333;
const int utcOffsetSeconds = 7200;

int ntpSyncInterval = 3600;
time_t prevNtpSyncTime = 0;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  rtc.begin();
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }
  udp.begin(123);
  setSyncProvider(getNtpTime);
  setSyncInterval(ntpSyncInterval);
}

void loop() {
  time_t now = tz.toLocal(now());
  currentWeather = getCurrentWeather(lat, lon, apiKey, server, &udp, utcOffsetSeconds);
  if (now > toTime_t(currentWeather.sunrise, utcOffsetSeconds) && now < toTime_t(currentWeather.sunset, utcOffsetSeconds)) {
  } else {
  }
  delay(1000);
}

time_t getNtpTime() {
  while (udp.parsePacket() > 0) {
  }
  udp.beginPacket(server, 123);
  udp.write(byte(0x1B));
  udp.endPacket();
  if (udp.parsePacket() == 0) {
    return 0;
  }
  unsigned long secsSince1900;
  udp.read((byte*)&secsSince1900, sizeof(secsSince1900));
  return secsSince1900 - 2208988800UL + utcOffsetSeconds;
}
```

