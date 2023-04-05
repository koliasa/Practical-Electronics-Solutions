# Основна мета проекту
Включати реле при настанні сутінків та вимикати його під час світанку. Для цього використовується модуль годинника реального часу DS3231 RTC, а також з'єднання зі світовим часом через NTP-сервер. Крім того, з метеостанції отримується інформація про погоду, що використовується для вимикання реле в разі досягнення певної температури.

Код включає в себе підключення необхідних бібліотек, оголошення констант і змінних, встановлення з'єднання з WiFi, підключення до NTP-сервера, отримання часу, налаштування часового поясу, отримання даних з метеостанції, а також управління реле.

Перша частина коду відповідає за підключення до WiFi та NTP-сервера, отримання часу і встановлення часового поясу:

```C++
#include <Wire.h>
#include <RTClib.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <WiFiUdp.h>
#include <TimeLib.h>
#include <Timezone.h>
#include <OpenWeatherMapCurrent.h>

const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";
const char* ntpServerName = "pool.ntp.org";
const int timeZone = 2;

IPAddress local_IP(192, 168, 1, 60);
IPAddress gateway(192, 168, 1, 1);
IPAddress subnet(255, 255, 255, 0);

WiFiUDP Udp;
unsigned int localPort = 8888;
time_t prevNtpSyncTime = 0;
const long ntpSyncInterval = 60 * 60 * 4;
RTC_DS3231 rtc;
```
Далі йде функція для отримання часу з NTP-сервера:

```C++
time_t getNtpTime() {
  while (Udp.parsePacket() > 0) ; // discard any previously received packets
  Serial.println("Transmit NTP Request");
  IPAddress ntpServerIP;
  WiFi.hostByName(ntpServerName, ntpServerIP);
  Serial.print(ntpServerName);
  Serial.print(": ");
  Serial.println(ntpServerIP);
  sendNTPpacket(ntpServerIP);
  uint32_t beginWait = millis();
  while (millis() - beginWait < 1500) {
    int size = Udp.parsePacket();
    if (size >= NTP_PACKET_SIZE) {
      Serial.println("Receive NTP Response");
      byte buffer[NTP_PACKET_SIZE];
```
Цей код реалізує автоматичне управління реле на основі вимірів освітленості та часу дня. Для цього використовується модуль годинника реального часу DS3231 RTC та фотодатчик.

Код розпочинається з ініціалізації модуля RTC та фотодатчика. Потім встановлюється час RTC з моменту компіляції коду, який зберігається в константі __TIME__ та __DATE__. Це дозволяє розрахувати час сходу та заходу сонця на основі дати та координат місця розташування.

У основному циклі програми спочатку вимірюється рівень освітленості, після чого порівнюється з пороговим значенням. Якщо рівень освітленості нижче порогового, то вмикається реле. Якщо рівень освітленості вище порогового, то реле вимикається.

При використанні фотодатчика необхідно налаштувати порогове значення, яке визначає, коли потрібно включати реле. Це можна зробити експериментальним шляхом шляхом зміни значення порогового рівня в коді та спостереженням за роботою системи.

Крім того, можливо покращити цей код, додавши в нього додаткові функції, такі як калібрування фотодатчика та налаштування параметрів підключення до мережі Wi-Fi.
