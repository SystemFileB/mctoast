# 注意：这个文件夹的1.png来自Minecraft Wiki，相关的版权归Mojang Studios所有

import mctoast
mctoast.init()
mctoast.new_toast(mctoast.ADVANCEMENT,"1.png",text1="进度已达成！",text2="甜蜜的梦") #后面的建议用关键字传参
mctoast.wait_no_toast() #实际使用中可能不会使用