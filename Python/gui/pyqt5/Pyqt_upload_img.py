from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout,QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
import sys
import os


class APP():
    # UI 主体构造部分
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Examable")
    window.setFixedWidth(800)
    window.setStyleSheet("background: #161219;")

    grid = QGridLayout()


    # we only have one frame
    # once we dealing with multiple frame, we have to create a global dictionary, append local widgets into it
    def main(self):
        # display logo
        self.image = QPixmap("/Users/jack/Desktop/Python/Py_project/Examable/Assets/Examable_logo_new.png")
        self.logo = QLabel()
        self.logo.setPixmap(image)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        logo.setStyleSheet("margin-top: -300px;")


        # Create a BUTTON WIDGET for upload image
        # 如果由多个object在图像中，需要谨慎加padding， margin。
        button = QPushButton("UPLOAD")
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet(
            "*{border: 6px solid '#FED7BE';" +
            "border-radius: 45px;" +
            "font-size: 35px;" +
            "color: 'white';" +
            "padding: 10px 0;" +
            "margin: 5px 15px}" +
            "*:hover{background: '#FED7BE';}"
        )
        button.clicked.connect(get_image)
        # 直接等于函数名字，即可应用函数，不需要加括号


        # Create a BUTTON2 WIDGET for output the answer, and the corresponding question.
        button2 = QPushButton("OUTPUT")
        button2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button2.setStyleSheet(
            "*{border: 6px solid '#FED7BE';" +
            "border-radius: 45px;" +
            "font-size: 35px;" +
            "color: 'white';" +
            "padding: 10px 0;" +
            "margin: 5px 15px}" +
            "*:hover{background: '#FED7BE';}"
        )


        grid.addWidget(logo, 0, 0)
        grid.addWidget(button, 1, 0)
        grid.addWidget(button2, 2, 0)

    def get_image(self):
        image_file = QFileDialog.getOpenFileName(None, 'open file', '/Users/jack', 'Image files (*.jpg *jpeg *png)')
        print(image_file)
        print(image_file[0])



if __name__ == "__main__":
    construct = APP()
    construct.setLayout(construct.grid)
    construct.show()
    sys.exit(app.exec_())