import time

start_time = time.localtime()
print(f"시작시간: {start_time.tm_hour}:{start_time.tm_min:02d}:{start_time.tm_sec:02d}")

count = 0

while True:
    minute = count // 60
    second = count % 60
    hour = minute // 60
    minute %= 60

    if hour < 10:
        print(f"0{hour}:{minute:02d}:{second:02d}")

    else:
        print(f"{hour}:{minute:02d}:{second:02d}")
        
    time.sleep(1)
    count += 1

    if count % (60 * 60) == 0:
        print(f"{hour}시간이 경과했습니다. 휴식을 권장드립니다.")

    if count % (60 * 60 * 5) == 0:
        print(f"{hour}시간이 경과했습니다. 반드시 휴식을 취하시길 바랍니다.")

    if hour == 99 and minute == 59 and second == 59:
        print("최대 시간이 되어 프로그램을 종료합니다.")
        end_time = time.localtime()
        print(f"종료 시간: {end_time.tm_hour}:{end_time.tm_min:02d}:{end_time.tm_sec:02d}")
        break