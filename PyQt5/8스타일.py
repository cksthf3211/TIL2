# setStyleSheet()을 이용하면 어플리케이션 안의 다양한 구성 요소들의 스타일을 자유롭게 꾸밀 수 있습니다.

## Ex 3-10. 스타일 꾸미기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        lbl_red = QLabel('Red')     # 라벨 만듬
        lbl_green = QLabel('Green') # 라벨 만듬
        lbl_blue = QLabel('Blue')   # 라벨 만듬

        lbl_red.setStyleSheet("color: red;"
                             "border-style: solid;"
                             "border-width: 2px;"
                             "border-color: #FA8072;"
                             "border-radius: 3px") # 선 두께
        
        lbl_green.setStyleSheet("color: green;"
                               "background-color: #7FFFD4")
        
        lbl_blue.setStyleSheet("color: blue;"
                              "background-color: #87CEFA;"
                              "border-style: dashed;" # 점선
                              "border-width: 3px;"
                              "border-color: #1E90FF")

        vbox = QVBoxLayout()        # 수직 박스 레이아웃(QVBoxLayout())을 이용해서 세 개의 라벨 위젯을 수직으로 배치
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)

        self.setLayout(vbox)

        self.setWindowTitle('Stylesheet')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())