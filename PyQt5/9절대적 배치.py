# 절대적 배치(Absolute positioning) 방식은 각 위젯의 위치와 크기를 픽셀 단위로 설정해서 배치

# 절대 배치 방식을 사용할 때는 다음의 제약을 이해하고 있어야 합니다.

# 창의 크기를 조절해도 위젯의 크기와 위치는 변하지 않는다.
# 다양한 플랫폼에서 어플리케이션이 다르게 보일 수 있다.
# 어플리케이션의 폰트를 바꾸면 레이아웃이 망가질 수 있다.
# 레이아웃을 바꾸고 싶다면 완전히 새로 고쳐야 하며, 이는 매우 번거롭다.

## Ex 4-1. 절대적 배치.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('Label1', self)
        label1.move(20, 20)
        label2 = QLabel('Label2', self)
        label2.move(20, 60)

        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)

        self.setWindowTitle('Absolute Positioning')
        self.setGeometry(300, 300, 400, 200)
        self.show()
        # 위치를 설정하기 위해 move() 메서드를 사용
        # 라벨(label1, label2)과 푸시버튼(btn1, btn2)의 x, y 좌표를 설정함으로써 위치를 조절
        # 좌표계는 왼쪽 상단 모서리에서 시작
        # x 좌표는 왼쪽에서 오른쪽으로 갈수록 커지고, y 좌표는 위에서 아래로 갈수록 커짐
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())