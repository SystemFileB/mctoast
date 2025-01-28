import mctoast
import sys
help="""
生成一个MCToast图片或者弹出一个Toast
用法：
    python -m mctoast <参数> [保存路径]

参数：
    --toast=<弹窗类型>,-t=<弹窗类型>  指定弹窗类型<0,1,2>
                                      0: 进度弹窗 (默认)
                                      1: 解锁配方弹窗
                                      2: 系统消息弹窗
    --image=<图片路径>,-i=<图片路径>  指定图片路径，默认""，即不显示图片
    --title=<标题>,-t1=<标题>         指定标题，默认"进度已达成！"
    --title-color=<颜色>,-c1=<颜色>   指定标题颜色，默认"yellow"，你也可
                                      以使用"#RRGGBB"颜色代码
    --text=<文本>,-t2=<文本>          指定文本，默认"MCToast示例"
    --text-color=<颜色>,-c2=<颜色>    指定文本颜色，默认"white"，你也可
                                      以使用"#RRGGBB"颜色代码
    --help,-h,-?                      显示帮助
    [保存路径]                        指定保存路径，默认""，即直接弹窗

显示位置:
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃ [--image] [--title,--title-color]  ┃
    ┃ [       ] [--text, --text-color]   ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    十分的直观 (

示例：
    python -m mctoast -t=0 -i=1.png -t1=进度已达成！ -c1=yellow -t2=MCToast -c2=white

    python -m mctoast -t=2 -t1=提示 "-t2=想不到吧 我有空格"

    python -m mctoast -t=0 -i=1.png -t1=进度已达成！ -c1=yellow "-t2=我好像被保存了. . ." -c2=white test.png

本mctoast具有超级牛力
"""
moo="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣾⣷⣾⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠁⠁⠈⠁⠀⠀⠀⠀⠀⢹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢹⣿⣿⡆⠀⠈⠥⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⢽⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⣶⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⡌⠀⠀⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡆⠀⣿⣾⣶⣆⠀⠀⢨⡄⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⡈⠛⢿⣿⣿⡄⠀⢸⢊⣀⠈⣿⣿⣶⣶⣤⣄⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠈⠀⠉⠁⠀⠀⠄⠀⠀⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀
⠀⠀⠀⠀⠀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡄⠲⠤⢤⣤⡄⠀⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧
⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣉⣀⣐⠒⠒⠠⠰⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠤⠤⠉⣉⣉⢸⣓⡲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠒⠒⠒⠠⠤⢼⣭⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣉⣙⠛⠒⢸⠶⣦⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠤⠬⢍⣉⣹⣛⣓⣲⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡒⠲⠶⠶⡿⣽⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣍⣙⣛⣏⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠦⠤⣬⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣙⣟⣿⣷⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆
⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠙⠃
⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠀⠀⠀
⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠛⠁⡇⠟⢿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀

Rickrolled LOL
"""
def mian():
    global help,moo
    print("MCToast 生成器 1.13\n")
    toasts=(mctoast.ADVANCEMENT,mctoast.RECIPE,mctoast.SYSTEM)
    toast=mctoast.ADVANCEMENT
    image=None
    text1="进度已达成！"
    color1="yellow"
    text2="MCToast示例"
    color2="white"
    savepath=None
    if len(sys.argv)>1:
        argv=sys.argv[1:]
        for arg in argv:
            if arg.startswith("--toast=") or arg.startswith("-t="):
                try:
                    toast=toasts[int(arg.split("=")[1])]
                except ValueError:
                    print("ERROR: 无效的Toast类型")
                    exit(1)
                print(toast)
            elif arg.startswith("--image=") or arg.startswith("-i="):
                if arg.split("=")[1].startswith("http"):
                    try:
                        from requests import get
                        import io
                    except ImportError:
                        print("ERROR: 未安装requests库，无法执行这个操作")
                        exit(1)
                    req=get(arg.split("=")[1])
                    image=io.BytesIO(req.content)

                else:
                    image=arg.split("=")[1]
            elif arg.startswith("--title=") or arg.startswith("-t1="):
                text1=arg.split("=")[1]
            elif arg.startswith("--title-color=") or arg.startswith("-c1="):
                color1=arg.split("=")[1]
            elif arg.startswith("--text=") or arg.startswith("-t2="):
                text2=arg.split("=")[1]
            elif arg.startswith("--text-color=") or arg.startswith("-c2="):
                color2=arg.split("=")[1]
            elif arg.startswith("--help") or arg.startswith("-h") or arg.startswith("-?"):
                print(help)
                exit(0)
            elif arg=="--moo":
                print(moo)
                exit(0)
            else:
                savepath=arg
    else:
        print("WARNING: 未指定参数，将弹出默认Toast，请使用 --help 查看帮助")
    if savepath==None:
        mctoast.init()
        mctoast.new_toast(toast,image,text1,color1,text2,color2)
        mctoast.wait_no_toast()
    else:
        mctoast.generate_image(toast,image,text1,color1,text2,color2,mctoast.RETURN_SAVETOFILE, False, savepath)
        print("已保存:",savepath)

if __name__=="__main__":
    mian()