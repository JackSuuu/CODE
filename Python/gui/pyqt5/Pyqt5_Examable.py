from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QFileDialog, QGridLayout, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import pyqtSlot
# from Examable_source_code import search_answer
import sys
import subprocess



# UI 主体构造部分
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Examable")
window.setFixedWidth(800)
window.setStyleSheet("background: #161219;")
grid_layout = QGridLayout()

# we only have one frame
# once we dealing with multiple frame, we have to create a global dictionary, append local widgets into it
def main():
    # display logo
    image = QPixmap("/Users/jack/Desktop/Python/Py_project/Examable/Assets/Examable_logo_new.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
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
    # button.clicked.connect(get_image)

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
    button2.clicked.connect(on_click)

    grid_layout.addWidget(logo, 0, 0)
    grid_layout.addWidget(button, 1, 0)
    grid_layout.addWidget(button2, 2, 0)


def get_image():
    image_file = QFileDialog.getOpenFileName(None, 'open file', '/Users/jack', 'Image files (*.jpg *jpeg *png)')
    print(image_file)
    print(image_file[0])
    # Ans_file = search_answer(image_file)
    # return Ans_file

Ans_file = get_image()

@pyqtSlot()
def on_click():
    if Ans_file != True:
        subprocess.call(('open', "/Users/jack/Desktop/Learning_Python.pdf", Ans_file))
    else:
        msg_box = QMessageBox(QMessageBox.Warning, 'ERROR', 'No target answer yet')
        msg_box.exec_()

# class Close(QWidget):
#     def closeEvent(self, event):
#         result = QMessageBox.question(self, "标题", "亲，你确定想关闭我?别后悔！！！'_'", QMessageBox.Yes | QMessageBox.No)
#         if (result == QMessageBox.Yes):
#             event.accept()
#             # 通知服务器的代码省略，这里不是重点...
#         else:
#             event.ignore()
#


if __name__ == "__main__":
    main()
    window.setLayout(grid_layout)
    window.show()
    sys.exit(app.exec_())




