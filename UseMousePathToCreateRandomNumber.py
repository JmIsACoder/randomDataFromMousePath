# coding: utf-8
"""
@File       :   mouse_path.py
@Author     :   jiaming
@Modify Time:   2021/5/9
@Contact    :   https://jiaming.blog.csdn.net/
@Version    :   1.0
@Desciption :   
"""
 
import time
import pyautogui as pag
x2 = y2 = -1
N = 10000000
try:
    while N:
        
        x1, y1 = pag.position()  # 返回鼠标的坐标
        if x2 != x1 or y2 != y1:
            x2 = x1; y2 = y1
            print("Press Ctrl-C to end, Position : (%s, %s)" % (x2, y2), end=" ")
            s = ""
            if x2 % 2 == 0 and y2 % 2 == 0 or x2 % 2 != 0 and y2 % 2 != 0:
                s = "1"
            else:
                s = "0"
            with open("random.txt", "a+") as f:
                f.write(s)
                print("写入%s, %d" % (s, N))
            N -= 1
            print()
        
except KeyboardInterrupt:
    print('end')

if __name__ == "__main__":
    pass

