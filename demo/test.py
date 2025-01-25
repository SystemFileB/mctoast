# 注意：这个文件夹的1.png来自Minecraft Wiki，相关的版权归Mojang Studios所有

import mctoast,time
mctoast.init()
mctoast.new_toast(mctoast.ADVANCEMENT,"1.png",text1="进度已达成！",text2="甜蜜的梦") #后面的建议用关键字传参
time.sleep(5)
mctoast.new_toast(mctoast.RECIPE,"1.png",text1="配方已解锁！",color1="green",text2="请检查你的配方书",color2="black")
time.sleep(5)
for i in range(20):
    mctoast.new_toast(mctoast.SYSTEM,text1="通知",text2="OHHHHHHHHHHHH")
    time.sleep(0.5)
mctoast.wait_no_toast() #实际使用中可能不会使用