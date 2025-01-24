#!/usr/bin/python3
import tkinter as tk
import os
import time
from PIL import Image, ImageDraw, ImageFont, ImageTk
import _thread as thread
from threading import Thread,Event
path=os.path.dirname(__file__)
pathjoin=os.path.join
toasts=[None,None,None,None,None]

# 定义常量
ADVANCEMENT = pathjoin(path, "assets","mctoast","textures","advancement.png")
RECIPE = pathjoin(path, "assets","mctoast","textures","recipe.png")
SYSTEM = pathjoin(path, "assets","mctoast","textures","system.png")

def generate_image(toast, image_path, text1, color1, text2, color2):
        """生成Toast图片"""
        # 打开背景图片并缩放
        background_image = Image.open(toast).resize((320, 64))
        
        # 打开小图片并缩放
        if image_path:
            small_image = Image.open(image_path).resize((30, 30))
            background_image.paste(small_image, (17, 17))
        
        # 创建一个绘图对象
        draw = ImageDraw.Draw(background_image)
        
        # 加载字体
        font = ImageFont.truetype(pathjoin(path,"assets","mctoast","fonts","unifont.otf"), 15)
        
        if toast==SYSTEM:
            if text1 and color1:
                draw.text((34, 13), text1, fill=color1, font=font)
            if text2 and color2:
                draw.text((34, 35), text2, fill=color2, font=font)
        else:
            # 在指定位置绘制文字
            if text1 and color1:
                draw.text((60, 13), text1, fill=color1, font=font)
            if text2 and color2:
                draw.text((60, 35), text2, fill=color2, font=font)
        
        # 将 Pillow 图片转换为 PhotoImage
        return ImageTk.PhotoImage(background_image)

class ToastWindowUI:
    def __init__(self, master=None, data_pool=None):
        # build ui
        self.root = tk.Tk(master)
        self.root.configure(
            background="#EEEEEE",
            borderwidth=0,
            height=200,
            takefocus=False,
            width=200)
        self.root.geometry("320x320+{}+0".format(self.root.winfo_screenwidth()-320))
        self.root.withdraw()
        self.root.overrideredirect("true")
        self.root.title("MCToast")
        self.root.attributes("-topmost", "true")
        self.root.attributes("-transparentcolor", "#EEEEEE")
        self.set_no_focus()
        self.set_no_focus()
        self.root.resizable(False, False)
        self.canvas = tk.Canvas(self.root, width=320, height=320, bg="#EEEEEE", highlightthickness=0)
        self.canvas.place(x=0,y=0)
    
    def set_no_focus(self):
        """设置窗口为无焦点窗口并穿透鼠标点击"""
        import ctypes
        if os.name == 'nt':  # Windows
            GWL_EXSTYLE = -20
            WS_EX_NOACTIVATE = 0x08000000
            WS_EX_TRANSPARENT = 0x00000020
            WS_EX_LAYERED = 0x00080000
            hwnd = ctypes.windll.user32.GetParent(self.root.winfo_id())
            style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
            style = style | WS_EX_NOACTIVATE | WS_EX_TRANSPARENT | WS_EX_LAYERED
            ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
            ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, 255, 0x00000002)
        elif os.name == 'posix':  # Linux
            self.root.wm_attributes('-type', 'splash')
    
    def main(self):
        tk.mainloop()

    def new_toast(self, toast=ADVANCEMENT, image_path=None, text1="一个弹窗", color1="yellow", text2="MCToast示例", color2="white",event=None):
        """弹出Toast，但是阻塞"""
        global toasts
        while True:
            for i in range(5):
                if toasts[i] == None:
                    # 使用 Pillow 生成图片
                    photo=generate_image(toast, image_path, text1, color1, text2, color2)
                    self.root.deiconify()
                    toasts[i] = self.canvas.create_image(320, i*64, anchor="nw", image=photo)
                    event.set()
                    x=320
                    speed=-1.96
                    while x>0:
                        x+=speed
                        self.canvas.move(toasts[i], speed, 0)
                        if speed<-0.1:
                            speed+=0.006
                        self.canvas.update()
                        time.sleep(0.0025)
                    self.canvas.move(toasts[i], 0, 0)
                    x=0
                    speed=0.1
                    time.sleep(2.5)
                    while x<320:
                        x+=speed
                        self.canvas.move(toasts[i], speed, 0)
                        if speed<2:
                            speed+=0.006
                        self.canvas.update()
                        time.sleep(0.0025)
                    self.canvas.delete(toasts[i])
                    toasts[i] = None
                    if toasts==[None,None,None,None,None]:
                        self.root.withdraw()
                    return
            time.sleep(0.2)
    
    def wait_no_toast(self):
        """等待所有Toast消失"""
        while True:
            if all(toast is None for toast in toasts):
                return
            time.sleep(0.2)
    
    def stop(self):
        self.root.destroy()
    
    def set_no_focus(self):
        """设置窗口为无焦点窗口"""
        import ctypes
        if os.name == 'nt':  # Windows
            GWL_EXSTYLE = -20
            WS_EX_NOACTIVATE = 0x08000000
            hwnd = ctypes.windll.user32.GetParent(self.root.winfo_id())
            style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
            style = style | WS_EX_NOACTIVATE
            ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
        elif os.name == 'posix':  # Linux
            self.root.wm_attributes('-type', 'splash')

window=None
def _init():
    global window
    window=ToastWindowUI()
    window.main()

def init():
    thread.start_new_thread(_init,())
    while type(window)!=ToastWindowUI:
        pass

def new_toast(toast=ADVANCEMENT, image_path=None, text1="一个弹窗", color1="yellow", text2="MCToast示例", color2="white"):
    global window
    #thread.start_new_thread(window.new_toast,(toast, image_path, text1, color1, text2, color2))
    #window.new_toast(toast, image_path, text1, color1, text2, color2)
    e=Event()
    t=Thread(target=window.new_toast,args=(toast, image_path, text1, color1, text2, color2, e))
    t.start()
    e.wait()

def quit():
    global window
    window.stop()

def wait_no_toast():
    global window
    window.wait_no_toast()

if __name__ == "__main__":
    # demo
    init()
    for i in range(1,11):
        new_toast(toast=SYSTEM, text2=f"第{i}")
        time.sleep(0.5)
    wait_no_toast()