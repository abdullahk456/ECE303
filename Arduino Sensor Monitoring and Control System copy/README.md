# Arduino Sensor Monitoring & Control System with Node-RED

This project implements a live, interactive sensor monitoring and control system using an Arduino Uno and the GY-87 IMU module, alongside an ultrasonic sensor and two LEDs. Developed as part of **ECE303: Embedded Systems & Interfacing** at Drexel University, the system demonstrates two-way communication between hardware and a user dashboard via serial and Node-RED integration.

## 🚀 Features

- Real-time temperature, motion, and distance monitoring
- GY-87 IMU sensor (temperature, accelerometer, gyroscope, barometer)
- HC-SR04 ultrasonic distance sensor
- Live data display on a Node-RED dashboard
- User control of red and blue LEDs from the dashboard
- Serial communication between Arduino and Node-RED
- Bi-directional interaction: sensor feedback + control commands

## 🧰 Hardware Used

- Arduino Uno (or compatible board)
- GY-87 IMU module
- HC-SR04 ultrasonic sensor
- 2 LEDs (Red and Blue) with resistors
- USB cable (for serial interface)
- Computer running Node-RED

## 📊 Software & Tools

- Arduino IDE
- Node-RED
- Serial communication over USB
- JSON-formatted messages