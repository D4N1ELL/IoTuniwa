# IoT Environment Monitoring System

## Project Overview

This project demonstrates the implementation of a reference IoT application designed to monitor environmental parameters such as temperature and humidity. It uses basic tools and technologies to simulate sensor data, transmit it via MQTT, and visualize it on a Node-RED dashboard. The goal is to provide a simple, scalable IoT solution deployable on various platforms including laptops and Raspberry Pi.

### Components

- **Python Script**: Runs locally to generate random temperature and humidity data.
- **MQTT Broker**: Acts as the communication hub for data exchange.
- **Node-RED Server**: Subscribes to the MQTT broker and displays the data in a user-friendly graphical interface.

### Technologies

- **Python**: For scripting data generation.
- **MQTT Protocol**: For lightweight messaging between devices.
- **Node-RED**: For flow-based data processing and dashboard visualization.
- **Docker**: For containerizing the MQTT broker and Node-RED server.

## MQTT Broker and Node-RED Configuration

### Setup

The MQTT broker and Node-RED server are containerized using Docker, which simplifies deployment and enhances scalability.

```bash
docker-compose up -d
