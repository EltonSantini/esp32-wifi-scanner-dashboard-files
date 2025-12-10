# ESP32 Wi-Fi Scanner + Mini Dashboard

An **ESP32-based Wi-Fi scanner** that discovers nearby access points and exposes results through a simple interface.

This project is meant as a learning and demo tool for:
- ESP32 Wi-Fi APIs
- Lightweight data collection
- Minimal dashboards for debugging / presence-style use-cases

> All examples use generic, non-sensitive Wi-Fi data.

---

## ✨ Features

- Periodic **Wi-Fi scans** for nearby APs:
  - SSID
  - BSSID (MAC)
  - RSSI (signal strength)
  - Channel
  - Timestamp
- Optional local **HTTP endpoint** on the ESP32 to view last scan
- Optional **backend** service (Python) to:
  - Receive scan results via HTTP
  - Append to JSON/CSV for later analysis
- Simple **HTML dashboard** to visualize scans

---

## 🚀 Getting Started

1. Flash `firmware/wifi_scanner.ino` to an ESP32 dev board.
2. (Optional) Run `backend/server.py` to accept scan POSTs.
3. Open `frontend/index.html` in a browser and point it at your data source.

See comments in each file for details.

---

## 📄 License

MIT.
