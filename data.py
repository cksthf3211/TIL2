import serial

ser = serial.Serial("COM4", 9600, timeout=1)


while True:
    try:
        ser.flushInput()
        rx_data = ser.readline().decode('ISO-8859-1').strip()
        if rx_data[5:11]:
            print(True)
            print(rx_data, rx_data[5:11]) 
            break

    except Exception as e:
        print("False:",e)
        break

ser.close()