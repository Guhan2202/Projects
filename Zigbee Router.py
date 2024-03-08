import serial
import time

# Configure serial port for Zigbee communication
zigbee_port = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

def send_alert(message):
    # Send alert message
    zigbee_port.write(message.encode())
    print("Message sent:", message)

def main():
    # Send alert message
    send_alert("School Zone, Maximum Speed: 40km")

if __name__ == "__main__":
    main()
