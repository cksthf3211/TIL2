import serial
import winsound

ser = serial.Serial("COM4", 19200, timeout=1)


while True:
    try:
        ser.flushInput()
        rx_data = ser.readline().decode('ISO-8859-1').strip()
        if rx_data != '':
            winsound.Beep(1800, 300)
            print(True)
            print(rx_data, rx_data[5:11]) 
            break

    except Exception as e:
        print("False:",e)
        break

ser.close()



import serial
import winsound

# ser = serial.Serial(port = 'COM4', 
#                     baudrate = 19200, 
#                     timeout = 0.5
#                     )

# while True:
#     try:
#         ser.flushInput() # 버퍼 비우기
#         # 데이터 읽어오기
#         rx_data = ser.readline().decode('ISO-8859-1').strip() # ISO-8859-1, UTF-8
#         if rx_data[5:11]:  # 6번째 위치부터 6자리수(S/N)
#             print("read_data(): 데이터를 읽었습니다.")
#             print(rx_data)
#             break
#     # 에러 예외처리
#     except UnicodeDecodeError:
#         print("read_data() - Error: 시리얼 데이터를 읽어올 수 없습니다.")
#         break

# ser.close()

# ----------------
# ser = serial.Serial("COM6", 9600, timeout=0.1)

# while True:
#     rx_barcode = ser.readline().decode().strip()
#     if len(rx_barcode) > 0:
#         print("read_barcode(): 바코드를 읽었습니다.")
#         print("Barcode number: ", rx_barcode)
#         break

# ser.close()

# 슬라이싱을 이용한 리더기 정보 출력
ser = serial.Serial("COM4", 19200, timeout=1)


while True:
    try:
        ser.flushInput()
        rx_data = ser.readline().decode('ISO-8859-1').strip()
        if rx_data != '':
            winsound.Beep(1800, 300)
            print(True)
            rx_data == 12345678
# &*01*230456*0*0*0000*0000*00000000*001036*2007*1807*2007*1807*0000*0*7C
            print(rx_data)
            print("ADR Reader Number:",rx_data[5:11])
            print("ADR Reader 선량값:",rx_data[26:34])
            print("ADR Reader 선량값:",rx_data[35:39] + '.' + rx_data[39:41])
            break

    except Exception as e:
        print("False:",e)
        break

ser.close()
