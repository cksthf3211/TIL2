import serial
import winsound

ser = serial.Serial(port = 'COM4', 
                    baudrate = 19200, 
                    timeout = 0.5
                    )

while True:
    try:
        ser.flushInput() # 버퍼 비우기
        rx = ser.readline().decode('ISO-8859-1').strip() # ISO-8859-1, UTF-8
        if rx[5:11]:
            winsound.Beep(2500, 700)
            print('result: True')
            print('data:', rx[5:11])
            break
            

    except UnicodeDecodeError:
        winsound.Beep(2000, 300)
        winsound.Beep(2000, 300)
        print('result: Flase')
        print("Error: 시리얼 데이터를 읽어올 수 없습니다.")
        rx = ''
        break

ser.close()
