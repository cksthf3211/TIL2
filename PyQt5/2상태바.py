import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setWindowTitle('Statusbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

# 메인창(Main window)은 메뉴바, 툴바, 상태바를 갖는 전형적인 어플리케이션 창
# 메인창은 QMenuBar, QToolBar, QDockWidget, QStatusBar를 위한 고유의 레이아웃을 갖고 있음.
# 가운데 영역에 중심위젯 (Central widget)을 위한 영역. 여기에는 어떠한 위젯도 들어올 수 있음