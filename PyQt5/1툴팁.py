from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('종료', self)
        btn.move(300, 720)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.closeEvent)

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        self.setWindowTitle('테스트 하자')
        self.setWindowIcon(QIcon('icon/포도.png'))  # 앱 아이콘
        self.setGeometry(1100, 100, 700, 800)
        
        self.setWindowTitle('종료 확인')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '종료 확인', '정말로 종료하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QCoreApplication.instance().quit()

if __name__ == '__main__':
    app = QApplication([])
    ex = MyWidget()
    app.exec_()