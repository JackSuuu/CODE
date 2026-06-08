import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

widgets = {
    "score": [],
    "question": [],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": []
}

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Legend of cs")
window.setFixedWidth(1000)
window.setStyleSheet("background: #161219;")

grid = QGridLayout()

# def clear_widget():
#     for widget in widgets:
#         if widgets[widget] != []:
#             widget[widget][-1].hide()
#         for i in range(0, len(widgets)):
#             widget[widget].pop()
#
# def show_frame1():
#     clear_widget()
#
# # how to switch by different frame
# def strart_game():
#     clear_widget()
#     frame2()


def create_buttons(answer, l_margin, r_margin):
    button = QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(400)
    button.setStyleSheet(
        "*{border: 4px solid '#FE7945';" +
        "margin-left:" + str(l_margin) + "px;" +
        "margin-right:" + str(r_margin) + "px;" +
        "font-size: 15px;" +
        "color: 'white';" +
        "padding: 20px 0;" +
        "margin-top: 10px}" +
        "*:hover{background: '#FE7945';}"
    )
    # button.clicked.connect(show_frame1())
    return button

def frame2():
    score = QLabel("80")
    score.setAlignment(QtCore.Qt.AlignHCenter)
    score.setStyleSheet(
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 20px 15px 0px 20px;" +
        "margin: 50px 100px;" +
        "background: '#FE7945';" +
        "border: 1px solid '#FE7945';" +
        "border-radius: 45px;"
    )
    widgets["score"].append(score)

    question = QLabel("Placeholder text will go here blah blah")
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        "font-size: 25px;" +
        "color: 'white';" +
        "padding: 75px;"
    )
    widgets["question"].append(question)

    button1 = create_buttons("answer1", 85, 5)
    button2 = create_buttons("answer2", 5, 85)
    button3 = create_buttons("answer3", 85, 5)
    button4 = create_buttons("answer4", 5, 85)

    widgets["answer1"].append(button1)
    widgets["answer2"].append(button2)
    widgets["answer3"].append(button3)
    widgets["answer4"].append(button4)



    grid.addWidget(widgets["score"][-1], 0, 1)
    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2)
    grid.addWidget(widgets["answer1"][-1], 2, 0)
    grid.addWidget(widgets["answer2"][-1], 2, 1)
    grid.addWidget(widgets["answer3"][-1], 3, 0)
    grid.addWidget(widgets["answer4"][-1], 3, 1)



frame2()

window.setLayout(grid)
window.show()
sys.exit(app.exec_())
