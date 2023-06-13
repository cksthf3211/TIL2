# 가장 일반적인 레이아웃 클래스는 '그리드 레이아웃(grid layout)'. 이 레이아웃 클래스는 위젯의 공간을 행 (row)과 열 (column)로 구분
# 그리드 레이아웃을 생성하기 위해 QGridLayout 클래스를 사용

## Ex 4-3. 그리드 레이아웃.
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit)

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()                     # QGridLayout을 만들고
        self.setLayout(grid)                     # 어플리케이션 창의 레이아웃으로 설정

        grid.addWidget(QLabel('Title:'), 0, 0)   # 세개의 라벨
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)
        # 세 개의 라벨을 첫 번째 열에 수직으로 배치합니다.

        grid.addWidget(QLineEdit(), 0, 1)        # 두개의 라인에디터
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)        # 한개의 텍스트에디터, 여러 줄의 텍스트를 수정할 수 있는 위젯. 세 번째 행, 두 번째 열에 배치

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())