# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PIL import Image

# 读取图片
guoqi = Image.open('imgs/guoqi.png')
touxiang = Image.open('imgs/20210930154653.jpg')

# 获取国旗的尺寸
x,y = guoqi.size
# 根据需求，设置左上角坐标和右下角坐标（截取的是正方形）
quyu = guoqi.crop((262,100, y+62,y-100))

# 获取头像的尺寸
w,h = touxiang.size
# 将区域尺寸重置为头像的尺寸
quyu = quyu.resize((w,h))
# 透明渐变设置
for i in range(w):
    for j in range(h):
        color = quyu.getpixel((i, j))
        alpha = 255-i//3
        if alpha < 0:
            alpha=0
        color = color[:-1] + (alpha, )
        quyu.putpixel((i, j), color)

# 粘贴到头像并保存
touxiang.paste(quyu,(0,0),quyu)
touxiang.save('五星红旗半透明渐变头像.png')

