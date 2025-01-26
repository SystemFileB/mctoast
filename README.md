# 🍞mctoast
一个基于tkinter的，用于显示minecraft风格的toast的库  
目前被[CamMoitor](https://github.com/SystemFileB/CamMonitor_Server)使用

## 📦安装
```shell
$ pip install mctoast pillow //现在我还没有上传pypi，你可以试试手动构建，或出门右转github action
$ pip install mctoast-1.0-py3-none-any.whl pillow //现在先用这个
```
我现在还不知道怎么实现自动安装pillow作为依赖😅，你只能手动装了 ()

## 🖼️画廊
原版效果:  
![原版](./img/game.gif)

mctoast模仿的效果:  
![mctoast](./img/lib.gif)

## ⚙️使用方法
见wiki

## ⚠️版权信息
- 这个库与Mojang,Microsoft**没有任何关系**，且在正式的库中(我在示范中使用了红色床的图片)**不使用**client.jar，.minecraft/assets文件夹下的**任何文件**    
- Toast纹理来自[VanillaXBR](https://modrinth.com/resourcepack/vanillaxbr)，基于[CC-BY-NC-4.0](https://creativecommons.org/licenses/by-nc/4.0/legalcode)许可证开源
- 若遇到了相关的许可证问题，请第一时间[提交issue](https://github.com/SystemFileB/mctoast/issues)并加上 版权或许可证问题 标签

## 更新日志
### 1.10.1
- 紧急修复：mctoast.init()报错

### 1.10
- 库的修改
&nbsp;&nbsp;&nbsp;&nbsp;- 为`generate_image`添加了默认值
&nbsp;&nbsp;&nbsp;&nbsp;- `generate_image(return_mode=RETURN_BYTE)`修复，现在返回的就是正常的图片字节
&nbsp;&nbsp;&nbsp;&nbsp;- 加入`generate_image(return_mode=RETURN_SAVETIFILE,filename="awasome.png")`语法，可以将图片保存为文件了
&nbsp;&nbsp;&nbsp;&nbsp;- 加入`generate_image(resize=False)`，在new_toast里使用的时候这个值为`True`，你一般不用修改，除非你也要把它缩放到320x64
- 允许你使用`python -m mctoast`生成toast图片或弹出toast
- <p style="color:gray">据说执行 python -m mctoast --moo 有彩蛋，你要不要试试</p>
- 移除了Herobrine (

### 1.01
- 修复：进度图片显示不正常

### 1.00
- 第一次发布