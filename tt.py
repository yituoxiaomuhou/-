import tkinter as tk
import random
import threading
import time

def dow():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0,width)
    b = random.randrange(0,height)
    window.title('187超级无敌大帅比祝你')
    window.geometry("380x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window,
             text = '婷婷宝贝天天开心，万事顺意ฅ(♡ơ ₃ơ)ฅ',
             bg = 'pink',
             font = ('楷体',16),
             width = 50,height = 40
             ).pack()
    window.mainloop()

threads = []
for i in range(200):
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.01)
    threads[i].start()