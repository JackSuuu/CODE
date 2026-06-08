import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        self.label = QLabel(self)
        self.label.setText("This is a text")
        self.label.setAlignment(Qt.AlignCenter)

        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")

        save = QAction("Save", self)
        save.setShortcut("Ctrl+1")
        file.addAction(save)

        edit = file.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")

        quit = QAction("Quit", self)
        quit.setShortcut("Ctrl+Q")
        file.addAction(quit)
        file.triggered[QAction].connect(self.processtrigger)

        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setWindowTitle("QMenubar")

    def processtrigger(self, q):
        print(q.text() + " is triggered")
        text = self.label.text()
        print(text)

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
