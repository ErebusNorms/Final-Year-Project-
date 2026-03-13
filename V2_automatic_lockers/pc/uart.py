import serial
import json
import time

ser = serial.Serial('COM4', 115200, timeout=1)  


def send_relay_command(locker_id, state):
    if ser is None:
        print("Serial port not available")
        return
    cmd = {"locker_id": locker_id, "state": state}
    try:
        ser.write((json.dumps(cmd) + '\n').encode('utf-8'))
        print(f"Sent command: {cmd}")
    except Exception as e:
        print(f"Error sending serial command: {e}")

try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print(f"Received: {line}")  # In dữ liệu nhận được từ ESP32
            send_relay_command(1, 1)
            time.sleep(2)
            send_relay_command(1, 0)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting program")
    ser.close()
