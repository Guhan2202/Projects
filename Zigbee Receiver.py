import serial
import time

# Configure serial port for Zigbee communication
zigbee_port = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

def receive_alert():
    # Check if data is available
    if zigbee_port.in_waiting > 0:
        received_message = zigbee_port.readline().decode().strip()
        
        # Check if received message contains the alert
        if "School Zone" in received_message and "Maximum Speed: 40km" in received_message:
            print("Alert received:", received_message)
            
            # Add your code here to react to the alert, such as displaying a warning to the driver

def main():
    while True:
        # Continuously check for incoming messages
        receive_alert()
        time.sleep(0.1)

if __name__ == "__main__":
    main()
