"""一个基于tkinter的，用于显示minecraft风格的toast的库  
目前被CamMoitor使用

这个库与Mojang,Microsoft没有任何关系，且在这里不使用client.jar，.minecraft/assets文件夹下的任何文件
Toast纹理来自VanillaXBR，基于CC-BY-NC-4.0许可证开源
若遇到了相关的许可证问题，请第一时间提交issue并加上 版权或许可证问题 标签

VanillaXBR: https://modrinth.com/resourcepack/vanillaxbr 
CC-BY-NC-4.0: https://creativecommons.org/licenses/by-nc/4.0/legalcode 
提交issue: https://github.com/SystemFileB/mctoast/issues """

import tkinter as tk
import os
import time
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageTk
from threading import Thread,Event
import _thread
path=os.path.dirname(__file__)
pathjoin=os.path.join
toasts=[None,None,None,None,None]

# 定义常量
ADVANCEMENT = pathjoin(path, "assets","mctoast","textures","advancement.png")
RECIPE = pathjoin(path, "assets","mctoast","textures","recipe.png")
SYSTEM = pathjoin(path, "assets","mctoast","textures","system.png")
RETURN_PHOTOIMAGE=0
RETURN_IMAGE=1
RETURN_BYTE=2
RETURN_SAVETOFILE=3

def generate_image(toast=ADVANCEMENT, image_path:str=None, text1="进度已达成！", color1="yellow", text2="MCToast示例", color2="white", return_mode=RETURN_IMAGE, resize:bool=False, filename:str=None):
    """生成Toast图片
    toast:str           背景图片(ADVANCEMENT,RECIPE,SYSTEM)
    image_path:str      图片路径(对应原版的物品位置)
    text1:str           第一行文本
    color1:str          第一行文本颜色
    text2:str           第二行文本
    color2:str          第二行文本颜色
    return_mode:int     返回模式(RETURN_IMAGE,RETURN_PHOTOIMAGE,RETURN_BYTE,RETURN_SAVETOFILE)
    filename:str        在return_mode=RETURN_SAVETOFILE时作为保存路径，未指定就报错
    """
    # 打开背景图片并缩放
    background_image = Image.open(toast)
    if background_image.mode != 'RGBA':
        background_image = background_image.convert("RGBA")
    
    # 打开小图片并缩放
    if image_path:
        small_image = Image.open(image_path).resize((57, 57),Image.Resampling.NEAREST)
        # 确保图片为RGBA模式
        if small_image.mode != 'RGBA':
            small_image = small_image.convert("RGBA")
        background_image.paste(small_image, (34, 33),mask=small_image)
    
    # 创建一个绘图对象
    draw = ImageDraw.Draw(background_image)
    
    # 加载字体
    font = ImageFont.truetype(pathjoin(path, "assets", "mctoast", "fonts", "unifont.otf"), 30)
    
    if toast == SYSTEM:
        if text1 and color1:
            draw.text((68, 26), text1, fill=color1, font=font)
        if text2 and color2:
            draw.text((68, 70), text2, fill=color2, font=font)
    else:
        # 在指定位置绘制文字
        if text1 and color1:
            draw.text((120, 26), text1, fill=color1, font=font)
        if text2 and color2:
            draw.text((120, 70), text2, fill=color2, font=font)
    if resize:
        background_image = background_image.resize((320, 64),Image.Resampling.NEAREST)
    # 将 Pillow 图片转换为 PhotoImage
    if return_mode==RETURN_IMAGE:
        return background_image
    elif return_mode==RETURN_BYTE:
        bytes=BytesIO()
        background_image.save(bytes,format="PNG")
        return bytes.getvalue()
    elif return_mode==RETURN_SAVETOFILE:
        if filename:
            background_image.save(filename)
        else:
            raise ValueError("未指定图片路径")

    else:
        return ImageTk.PhotoImage(background_image)

class ToastWindowUI:
    """Toast界面类"""
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
        self.root.resizable(False, False)
        self.canvas = tk.Canvas(self.root, width=320, height=320, bg="#EEEEEE", highlightthickness=0)
        self.canvas.place(x=0,y=0)
    
    def main(self):
        tk.mainloop()

    def new_toast(self, toast=ADVANCEMENT, image_path=None, text1="一个弹窗", color1="yellow", text2="MCToast示例", color2="white",event=None):
        """弹出Toast，但是阻塞"""
        global toasts
        while True:
            for i in range(5):
                if toasts[i] == None:
                    # 使用 Pillow 生成图片
                    photo=generate_image(toast, image_path, text1, color1, text2, color2, RETURN_PHOTOIMAGE, True)
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
    """别调用"""
    global window
    window=ToastWindowUI()
    window.main()

def init():
    """初始化窗口"""
    _thread.start_new_thread(_init,())
    while window==None:
        time.sleep(0.01)

def new_toast(toast=ADVANCEMENT, image_path:str=None, text1="一个弹窗", color1="yellow", text2="MCToast示例", color2="white"):
    """新弹窗
    toast:str           背景图片(ADVANCEMENT,RECIPE,SYSTEM)
    image_path:str      图片路径(对应原版的物品位置)
    text1:str           第一行文本
    color1:str          第一行文本颜色
    text2:str           第二行文本
    color2:str          第二行文本颜色"""
    global window
    e=Event()
    t=Thread(target=window.new_toast,args=(toast, image_path, text1, color1, text2, color2, e))
    t.start()
    e.wait()

def quit():
    """退出(好像根本不需要)"""
    global window
    window.stop()

def wait_no_toast():
    """等待所有toast消失"""
    global window
    window.wait_no_toast()