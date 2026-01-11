#include <WiFi.h>
#include <HTTPClient.h>
#include <math.h>

// Pins
const int dustPin = 34;
const int mq7Pin = 35;
const int mq135Pin = 32;
const int dustLed = 27;

// Calibration
float dustOffset = 0.065;
const float RLOAD = 10.0;
const float R0 = 35.0;

// WiFi
const char* ssid = "YOUR_WIFI_NAME";
const char* password = "YOUR_WIFI_PASSWORD";
const char* serverURL = "http://192.168.1.100:8000/sensor-data";

void setup() {
  Serial.begin(9600);
  pinMode(dustLed, OUTPUT);
  digitalWrite(dustLed, HIGH);

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi connected!");
}

void loop() {

  // ---- PM2.5 ----
  digitalWrite(dustLed, LOW);
  delayMicroseconds(280);
  float dustV = analogRead(dustPin) * (3.3 / 4095.0);
  delayMicroseconds(40);
  digitalWrite(dustLed, HIGH);

  float pm25 = ((dustV - dustOffset) * 200.0) / 1225.0;
  if (pm25 < 0) pm25 = 0;

  // ---- CO ----
  float coV = analogRead(mq7Pin) * (3.3 / 4095.0);
  float co = (coV - 0.15) * 100.0;
  if (co < 0) co = 0;

  // ---- MQ135 ----
  float mq135V = analogRead(mq135Pin) * (3.3 / 4095.0);
  float rs = ((3.3 * RLOAD) / mq135V) - RLOAD;
  float ratio = rs / R0;

  float nh3 = 102.2 * pow(ratio, -2.47);
  float no2 = 44.2 * pow(ratio, -2.89);

  // ---- JSON Payload ----
  String payload = "{";
  payload += "\"pm25\":" + String(pm25, 2) + ",";
  payload += "\"co\":" + String(co, 2) + ",";
  payload += "\"nh3\":" + String(nh3, 2) + ",";
  payload += "\"no2\":" + String(no2, 2);
  payload += "}";

  // ---- HTTP POST ----
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverURL);
    http.addHeader("Content-Type", "application/json");

    int httpResponseCode = http.POST(payload);

    Serial.print("HTTP Response: ");
    Serial.println(httpResponseCode);

    http.end();
  }

  delay(4000);
}
