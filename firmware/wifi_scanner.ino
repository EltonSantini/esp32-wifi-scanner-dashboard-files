#include <WiFi.h>

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("ESP32 Wi-Fi Scanner starting...");
}

void loop() {
  Serial.println("\nScanning for Wi-Fi networks...");

  int n = WiFi.scanNetworks();
  if (n == 0) {
    Serial.println("No networks found.");
  } else {
    Serial.printf("Found %d networks:\n", n);
    for (int i = 0; i < n; ++i) {
      Serial.printf("%d: %s (%d dBm) ch:%d\n",
                    i + 1,
                    WiFi.SSID(i).c_str(),
                    WiFi.RSSI(i),
                    WiFi.channel(i));
    }
  }

  delay(10000);
}
