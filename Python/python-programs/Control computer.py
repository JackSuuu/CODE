import pyautogui
import pyperclip
import time

array = ["Time is money money is time",
             "Are you angry?",
             "Focus On the definition",
             "Get some Vitamin D",
             "Life Is Wonderful",
             "Not SO?",
             "Don't say sorry",
             "Sorry means you'll do it again",
             "Focus on the AIM of the question",
             "Are you writing a love story?",
             "you always running to the wall"]

time.sleep(3)
x = 0

for i in range(100):
    if x <= 10:
        pyperclip.copy(array[x])  # 复制内容到剪贴板
        pyautogui.hotkey('command', 'v')  # 按下 ctrl + v 粘贴内容
        pyautogui.hotkey('return')
        x += 1
    else:
        x = 0


