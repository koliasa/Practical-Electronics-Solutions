#include <SoftwareSerial.h>

SoftwareSerial SIM800L(2, 3); // RX, TX

void setup() {
  Serial.begin(9600);
  SIM800L.begin(9600);
  delay(1000);

  // Set the SMS mode to text mode
  SIM800L.println("AT+CMGF=1");
  delay(500);

  // Enable the module to forward received SMS messages as URCs
  SIM800L.println("AT+CNMI=2,2,0,0,0");
  delay(500);

  Serial.println("SIM800L module initialized");
}

void loop() {
  if (SIM800L.available()) {
    String message = SIM800L.readString();
    if (message.indexOf("+CMT:") >= 0) {
      // Extract the sender's phone number and the message body
      int comma1 = message.indexOf(",");
      int comma2 = message.indexOf(",", comma1 + 1);
      String sender = message.substring(comma1 + 2, comma2 - 1);
      String body = message.substring(comma2 + 2);

      Serial.println("Received SMS message from " + sender);
      Serial.println("Message body: " + body);

      // Process the SMS command
      if (body == "ON") {
        digitalWrite(13, HIGH); // Turn on LED on pin 13
        sendSMS(sender, "LED turned on");
      } else if (body == "OFF") {
        digitalWrite(13, LOW); // Turn off LED on pin 13
        sendSMS(sender, "LED turned off");
      } else {
        sendSMS(sender, "Invalid command");
      }
    }
  }
}

void sendSMS(String recipient, String message) {
  SIM800L.println("AT+CMGS=\"" + recipient + "\"");
  delay(500);
  SIM800L.print(message);
  delay(500);
  SIM800L.write(26);
  delay(500);
}