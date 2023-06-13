# 박스 레이아웃 클래스를 이용하면 훨씬 유연하고 실용적인 레이아웃

# QHBoxLayout, QVBoxLayout은 여러 위젯을 수평으로 정렬하는 레이아웃 클래스
# QHBoxLayout, QVBoxLayout 생성자는 수평, 수직의 박스를 하나 만드는데, 다른 레이아웃 박스를 넣을 수도 있고 위젯을 배치

# 예제 코드에서 위젯의 가운데 아래 부분에 두 개의 버튼을 배치하기 위해 수평, 수직의 박스를 하나씩 사용
# 필요한 공간을 만들기 위해 addStretch() 메서드를 사용하고, 'stretch factor'를 조절

## Ex 4-2. 박스 레이아웃.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton('네')
        cancelButton = QPushButton('취소')

        hbox = QHBoxLayout() # 수평 박스를 하나 만들고, 두 개의 버튼과 양 쪽에 빈 공간을 추가
        hbox.addStretch(1)   # addStretch() 메서드는 신축성있는 빈 공간을 제공
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)   # 두 버튼 양쪽의 stretch factor가 1로 같기 때문에 이 두 빈 공간의 크기는 창의 크기가 변화해도 항상 같음

        vbox = QVBoxLayout() # 다음으로 수평 박스(hbox)를 수직 박스(vbox)에 넣어줌
        vbox.addStretch(3)   # 수직 박스의 stretch factor는 수평 박스를 아래쪽으로 밀어내서 두 개의 버튼을 창의 아래쪽에 위치
        vbox.addLayout(hbox)
        vbox.addStretch(1)   # 이 때에도 수평 박스 위와 아래의 빈 공간의 크기는 항상 3:1을 유지합니다. stretch factor를 다양하게 바꿔보면, 의미를 잘 이해

        self.setLayout(vbox)
        # 최종적으로 수직 박스를 창의 메인 레이아웃으로 설정

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())