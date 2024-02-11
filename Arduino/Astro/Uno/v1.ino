#include <DHT.h>
#include <Wire.h>
#include <RTClib.h>

#define DHTPIN 2     // пін, до якого підключений датчик DHT11
#define DHTTYPE DHT11   // використовуємо датчик DHT11
DHT dht(DHTPIN, DHTTYPE);

RTC_DS1307 rtc;    // створюємо об'єкт для роботи з RTC DS1307

const int RELAY_PIN = 3;  // пін, до якого підключене реле
const int DARK_THRESHOLD = 200; // порігове значення для визначення сутінків
const int LIGHT_THRESHOLD = 700; // порігове значення для визначення світлоти
const int ON_HOUR = 18; // година, коли вмикається світло
const int OFF_HOUR = 6; // година, коли вимикається світло

void setup() {
  Serial.begin(9600);
  dht.begin();
  Wire.begin();
  rtc.begin();
  pinMode(RELAY_PIN, OUTPUT);
}

void loop() {
  DateTime now = rtc.now();
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  int light = analogRead(A0); // читаємо дані з фоторезистора

  // перевірка, чи настав час вмикання світла
  if (now.hour() >= ON_HOUR && now.hour() < OFF_HOUR) {
    if (light < DARK_THRESHOLD) { // перевіряємо, чи настали сутінки
      digitalWrite(RELAY_PIN, HIGH); // вмикаємо світло
    } else if (light > LIGHT_THRESHOLD) { // перевіряємо, чи настали денні години
      digitalWrite(RELAY_PIN, LOW); // вимикаємо світло
    }
  } else { // якщо наступив час вимкнення світла
    digitalWrite(RELAY_PIN, LOW); // вимикаємо світло
  }
  
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print("°C, Humidity: ");
  Serial.print(humidity);
  Serial.print("%, Light: ");
  Serial.print(light);
  Serial.println(" lx");

  delay(5000);
}
