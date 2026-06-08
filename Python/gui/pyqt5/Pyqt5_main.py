from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout,QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
import sys
import os

# if require different layer of frame, so it requires a gloabl frame
widgets = {
    "logo": [],
    "button": [],
    "button2": [],
}


# UI 主体构造部分
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Examable")
window.setFixedWidth(800)
window.setStyleSheet("background: #161219;")

grid = QGridLayout()


# we only have one frame
# once we dealing with multiple frame, we have to create a global dictionary, append local widgets into it
def frame():
    # display logo
    image = QPixmap("/Users/jack/Desktop/Python/Py_project/Examable/Assets/Examable_logo_new.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: -300px;")
    # widgets["logo"].append(logo)

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
    # button.clicked.connect()
    # widgets["button"].append(button)


    #  Create a BUTTON2 WIDGET for output the answer, and the corresponding question.
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
    # widgets["button2"].append(button2)

    # Place the widget to the correct position
    # grid.addWidget(widgets["logo"][-1], 0, 0)
    # grid.addWidget(widgets["button"][-1], 1, 0)
    # grid.addWidget(widgets["button2"][-1], 2, 0)

    grid.addWidget(logo, 0, 0)
    grid.addWidget(button, 1, 0)
    grid.addWidget(button2, 2, 0)

# get file name
# def file():
#     file_name = QFileDialog.getOpenFileNames(QWidget =, 'choose image', os.getcwd(),)
#     print(file_name)
#     print(file_name[0]) # the key to import the file name for finding the image


if __name__ == "__main__":
    frame()
    window.setLayout(grid)
    window.show()
    sys.exit(app.exec_())