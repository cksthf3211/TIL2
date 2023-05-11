import serial

ser = serial.Serial("COM7", 9600, timeout=1)

rx = ''
while True:
    rx = ser.readline().decode('ascii')
    
    if (len(rx) > 0):
        print(rx)
        break

ser.close()