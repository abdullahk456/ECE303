# Wireless Sensor Monitoring and Control System (Station Mode Upgrade)

This project showcases a fully integrated, closed-loop wireless control system built using an Arduino Uno R4 WiFi, sensor modules, and a user interface. Originally developed as two assignments in **ECE303: Embedded Systems & Interfacing** at Drexel University, this combined version enhances the system by upgrading to **Station Mode**, enabling mobile access over a local Wi-Fi network.

## 🚀 Features

- Wireless sensor data acquisition using Arduino Uno R4 WiFi
- Real-time communication between Arduino, Node-RED dashboard, and a Python client
- Closed-loop control system with live feedback and decision-based LED actuation
- Station Mode integration for Wi-Fi access and control via mobile phone
- Interactive web-based dashboard (Node-RED) for control and monitoring

## 🧰 Hardware Used

- Arduino Uno R4 WiFi
- GY-87 IMU sensor module (for temperature, acceleration, gyroscope)
- HC-SR04 ultrasonic distance sensor
- Red and blue LEDs
- Resistors, jumper wires
- Access to Wi-Fi router

## 🛠 Software & Tools

- Arduino IDE
- Node-RED
- Python (for optional client interaction)
- Serial and Wi-Fi communication (JSON over HTTP/Serial)
- Web browser (for dashboard access)

## 🧠 System Architecture

1. **Sensor Layer (Arduino):**  
   Reads motion, temperature, and distance data. Based on sensor input or dashboard control, it dynamically toggles LEDs.

2. **Control Interface (Node-RED):**  
   Receives sensor data and sends commands via Wi-Fi to Arduino. Users interact with a web-based dashboard.

3. **Python Client (Optional):**  
   Can parse JSON responses and issue commands as part of system testing or automation.

## 📡 Station Mode Functionality

- Arduino connects to your home Wi-Fi network (Station Mode)
- IP address is assigned and displayed via serial monitor
- Dashboard access and control can be done through any device on the same network (e.g., mobile phone browser)