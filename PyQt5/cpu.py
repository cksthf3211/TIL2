import sys
import psutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
import matplotlib.pyplot as plt

print(psutil.cpu_percent())
print(psutil.virtual_memory())
print(psutil.disk_usage('/'))
print(psutil.net_io_counters())

print(psutil.cpu_percent()) # CPU사용률 백분율
print(psutil.cpu_stats())   # 컨텍스트 스위치, 인터럽트, 스프트웨어 인터럽트 및 시스템 호출 = CPU통계
print(psutil.cpu_freq())    # MHz단위로 현재, 최소 및 최대 CPU주파수 제공


class ResourceMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Resource Monitor')
        self.setGeometry(1100, 100, 700, 800)
        
        # 원형 차트를 표시할 QLabel 위젯 작성
        self.chart_label = QLabel(self)
        self.chart_label.setGeometry(50, 50, 600, 600)
        
        self.update_chart()
        self.show()

    def update_chart(self):
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory().percent
        disk_percent = psutil.disk_usage('/').percent
        network_percent = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

        # 값이 0인지 확인하고 목록에서 해당 레이블을 제거
        labels = ['CPU', 'Memory', 'Disk', 'Network']
        values = [cpu_percent, memory_percent, disk_percent, network_percent]
        for i in range(len(values)):
            if values[i] == 0:
                labels.pop(i)
                values.pop(i)

        colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
        wedgeprops = {'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

        # matplotlib을 사용하여 원형 차트를 만들고 임시 파일에 저장
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, colors=colors, wedgeprops=wedgeprops, shadow=True)
        ax.axis('equal')
        plt.savefig('chart.png')

        # 파일에서 차트 이미지를 로드하고 QLabel 위젯의 pixmap으로 설정
        chart_pixmap = QIcon('chart.png').pixmap(600, 600)
        self.chart_label.setPixmap(chart_pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    monitor = ResourceMonitor()
    sys.exit(app.exec_())