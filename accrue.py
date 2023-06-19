# 1일 누적 선량
def day(pk, adr_number):
    try:
        nremprt1 = Nremprt1.objects.get(pk=pk)
        current_date = datetime.datetime.now().date()

        total = 0
        if current_date:

            qrad_day_value = int(adr_number[26:34])
            total += qrad_day_value
            nremprt1.qrad_day = total

            print("day클래스이상무",nremprt1.qrad_day)


    except Nremprt1.DoesNotExist as e:
        print(e)


# 1주일 누적 선량
def week(pk):
    try:
        nremprt1 = Nremprt1.objects.get(pk=pk)

        qrad_week_data = deque()

        # 데이터 추가
        day_result = day(pk, adr_number)
        
        if day_result is not None:
            qrad_week_data.append(day_result)
        
        # 데이터가 7일을 넘어가면 가장 오래된 데이터 제거
        if len(qrad_week_data) > 7:
            qrad_week_data.popleft()

        nremprt1.qrad_week = sum(qrad_week_data)
        
        print('week클래스이상무',nremprt1.qrad_week)
        

    except Nremprt1.DoesNotExist as e:
        print(e)

# 1년 누적 선량
def year(pk):
    try:
        nremprt1 = Nremprt1.objects.get(pk=pk)

        qrad_yy_data = deque()

        # 데이터 추가
        day_result = day(pk, adr_number)
        
        if day_result is not None:
            qrad_yy_data.append(day_result)
        
        # 데이터가 365일을 넘어가면 가장 오래된 데이터 제거
        if len(qrad_yy_data) > 365:
            qrad_yy_data.popleft()

        nremprt1.qrad_yy = sum(qrad_yy_data)
        
        print('year클래스이상무',nremprt1.qrad_yy)
        

    except Nremprt1.DoesNotExist as e:
        print(e)


# 5년 누적 선량
def year_5(pk):
    try:
        nremprt1 = Nremprt1.objects.get(pk=pk)

        qrad_5y_data = deque()

        # 데이터 추가
        day_result = day(pk, adr_number)
        
        if day_result is not None:
            qrad_5y_data.append(day_result)
        
        # 데이터가 365일을 넘어가면 가장 오래된 데이터 제거
        if len(qrad_5y_data) > (365*5):
            qrad_5y_data.popleft()

        nremprt1.qrad_5y = sum(qrad_5y_data)
        
        print('year_5클래스이상무',nremprt1.qrad_5y)
        

    except Nremprt1.DoesNotExist as e:
        print(e)


# 월별 누적 선량
def month(pk):
    try:
        nremprt1 = Nremprt1.objects.get(pk=pk)

        qrad_mm = [nremprt1.qrad_mm1, nremprt1.qrad_mm2,
                   nremprt1.qrad_mm3, nremprt1.qrad_mm4,
                   nremprt1.qrad_mm5, nremprt1.qrad_mm6,
                   nremprt1.qrad_mm7, nremprt1.qrad_mm8,
                   nremprt1.qrad_mm9, nremprt1.qrad_mm10,
                   nremprt1.qrad_mm11, nremprt1.qrad_mm12]

        current_month = datetime.datetime.now().month # 6

        total = 0

        if current_month:
            mm = qrad_mm[current_month - 1]
            day_value = day(pk, adr_number)

            if day_value is not None:
                total += int(day_value)

                total = qrad_mm[current_month - 1]

            print('month클래스이상무', total) #qrad_mm (1~12월까지 다 출력)
        
    except Nremprt1.DoesNotExist as e:
        print(e)