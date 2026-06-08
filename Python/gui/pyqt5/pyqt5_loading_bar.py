import sys
import time

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QGridLayout
from PyQt5.QtCore import QBasicTimer


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background: #161515;")
        self.resize(500, 300)
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)
        # 载入进度条控件
        self.pgb = QProgressBar(self)
        self.pgb.setStyleSheet(
            "QProgressBar { border: 2px solid '#FED7BE'; "
            "border-radius: 5px; color: #FED7BE;  "
            "background-color: #161515; text-align: center;}"
            "QProgressBar::chunk {background-color: #FED7BE; "
            "border-radius: 10px; margin: 0.1px;  width: 1px;}"
        )

        # 设置一个值表示进度条的当前进度
        self.pv = 0

        # 申明一个时钟控件
        self.timer1 = QBasicTimer()

        # 设置进度条的范围
        self.pgb.setMinimum(0)
        self.pgb.setMaximum(100)
        self.pgb.setValue(self.pv)

        # 设置进度条文字格式
        self.pgb.setFormat('Loaded  %p%'.format(
            self.pgb.value() - self.pgb.minimum()))

        # 加载pushbutton1
        self.btn_start = QPushButton("begin", self)
        self.btn_start.setStyleSheet(
            "*{border: 3px solid '#FED7BE';" +
            "border-radius: 35px;" +
            "font-size: 10px;" +
            "color: 'white';" +
            "padding: 5px 0;" +
            "margin: 1px 5px}"
        )
        self.btn_start.clicked.connect(self.myTimerState)

        # 加载 pushbutton 2
        self.btn_update = QPushButton("update", self)
        self.btn_update.setStyleSheet(
            "*{border: 3px solid '#FED7BE';" +
            "border-radius: 35px;" +
            "font-size: 10px;" +
            "color: 'white';" +
            "padding: 5px 0;" +
            "margin: 1px 5px}"
        )
        self.btn_update.clicked.connect(self.update_event)

        grid_layout.addWidget(self.pgb, 0, 0)
        grid_layout.addWidget(self.btn_start, 1, 0)
        grid_layout.addWidget(self.btn_update, 2, 0)

    def myTimerState(self):
        if self.timer1.isActive():
            self.timer1.stop()
            self.btn_start.setText("begin")
        else:
            self.timer1.start(100, self)
            self.btn_start.setText("stop")

    def timerEvent(self, e):
        if self.pv == 100:
            self.timer1.stop()
            self.btn_start.setText("Finish")
        else:
            self.pv += 1
            self.pgb.setValue(self.pv)
            time.sleep(0.5)

    def update_event(self):
        if self.timer1.isActive():
            self.timer1.stop()
        self.btn_start.setText("begin")
        self.pv = 0
        self.pgb.setValue(self.pv)

    def refresh(self):
        for i in range(10):
            return i


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mytask = MyClass()
    mytask.show()
    app.exec_()
