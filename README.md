# 🍞mctoast
一个基于tkinter的，用于显示minecraft风格的toast的库  
目前被[CamMoitor](https://github.com/SystemFileB/CamMonitor_Server)使用

## 📦安装
```shell
# 从PyPI上安装
$ pip install mctoast
# 安装快照 (请将后面的路径换为实际的)
$ pip install /path/to/mctoast-wheel.whl
# 从github仓库安装 (有时候未经测试，也有可能无法运行)
$ pip install git+https://github.com/SystemFileB/mctoast.git@main
```
推荐你额外安装requests，这样你就可以在`-i=`参数中使用URL了
```shell
$ pip install requests
```

## 🖼️画廊
原版效果:  
![原版](./img/game.gif)

mctoast模仿的效果:  
![mctoast](./img/lib.gif)

## ⚙️使用方法
见wiki

## ⚠️版权信息
- 这个库与Mojang,Microsoft**没有任何关系**，且在正式的库中(我在示范中使用了红色床的图片)**不使用**client.jar，.minecraft/assets文件夹下的**任何文件**    
- Toast纹理来自[VanillaXBR](https://modrinth.com/resourcepack/vanillaxbr)，基于[CC-BY-NC-4.0](https://creativecommons.org/licenses/by-nc/4.0/legalcode)许可证
- 字体使用了GNU Unifont，基于[GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html)许可证
- 若遇到了相关的许可证问题，请第一时间[提交issue](https://github.com/SystemFileB/mctoast/issues)并加上 版权或许可证问题 标签

## 📰更新日志
### 1.20
- 命令行工具的修改
    - 如果你安装了requests，你就可以在`-i=`参数中使用网络图片
- 库的修改
    - 放宽了`generate_image` `image`参数的类型，现在只要是Pillow支持的都可以，如果Pillow不支持Pillow就会报错，命令行工具也是
    - 所以遇到`PIL.UnidentifiedImageError: cannot identify image file`你也不必上传issue，否则我就会把它标为 不予理会

### 1.12
- 紧急修复：setup.py并没有包含`__init__.py`和`__main__.py`文件，导致无法使用
- 重新加入1.11的更改
- 修复：python -m mctoast无法弹出参数自定义的toast

### 1.11.1
- 紧急修复：撤回1.11的更改

### 1.11
- 允许你直接运行mctoast，而非python -m mctoast

### 1.10.2
- 因为PyPI无法上传同一个版本的库，我又更改了这个库的README，所以我改了版本号

### 1.10.1
- 紧急修复：mctoast.init()报错

### 1.10
- 库的修改  
    - 为`generate_image`添加了默认值 
    - `generate_image(return_mode=RETURN_BYTE)`修复，现在返回的就是正常的图片字节  
    - 加入`generate_image(return_mode=RETURN_SAVETIFILE,filename="awasome.png")`语法，可以将图片保存为文件了  
    - 加入`generate_image(resize=False)`，在new_toast里使用的时候这个值为`True`，你一般不用修改，除非你也要把它缩放到320x64  
- 允许你使用`python -m mctoast`生成toast图片或弹出toast
- <p style="color:gray">据说执行 python -m mctoast --moo 有彩蛋，你要不要试试</p>
- 移除了Herobrine (

### 1.01
- 修复：进度图片显示不正常

### 1.00
- 第一次发布