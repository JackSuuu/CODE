import tkinter
import time
 
star=time.time()

def gettime(): 
    elap=time.time()-star# 获取时间差
    minutes = int(elap/60)
    seconds = int(elap-minutes*60.0)
    var.set('%02d:%02d' %(minutes, seconds))
    root.after(1, gettime)# 每隔1ms调用函数自身获取时间

root = tkinter.Tk()
root.title('电子时钟')

var=tkinter.StringVar()
lb=tkinter.Label(root, textvariable=var, fg='black', font=("Arial", 100))# 设置字体大小颜色
lb.pack()
gettime()

root.mainloop()


