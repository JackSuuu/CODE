
import easygui as gui
import sys

while 1:
    gui.msgbox('嗨，欢迎进入第一个界面小游戏o∩_∩o ')
    msg = '请问你喜欢吃什么水果？'
    title = "小游戏互动"
    choices = ["苹果", "桃子", "葡萄", "香蕉"]
    choice = gui.choicebox(msg, title, choices)
    gui.msgbox("你选择的是："+str(choice), "结果")
    msg = "你希望重新开始小游戏么"
    title = "请选择"
    if gui.ccbox(msg, title):
        pass
    else:
        sys.exit(0)
