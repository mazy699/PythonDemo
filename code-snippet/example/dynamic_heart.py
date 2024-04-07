import tkinter as tk
import time

# 定义一个函数来绘制心形


def draw_heart(canvas, x, y, size):
    canvas.create_arc(x - size, y - size, x + size, y + size, start=0,
                      extent=180, style='pieslice', outline='red', width=2)
    canvas.create_arc(x - size, y - size, x + size, y + size, start=180,
                      extent=180, style='pieslice', outline='red', width=2)
    canvas.create_line(x - size, y - size, x, y -
                       size * 0.8, fill='red', width=2)
    canvas.create_line(x + size, y - size * 0.8, x,
                       y - size, fill='red', width=2)
    canvas.create_line(x, y - size, x, y + size, fill='red', width=2)
    canvas.create_line(x - size * 0.8, y + size, x + size *
                       0.8, y + size, fill='red', width=2)
    canvas.create_line(x, y + size, x, y - size * 0.8, fill='red', width=2)

# 定义一个函数来更新心形的大小


def update_heart(canvas, x, y, size, dx, dy):
    size -= 1
    if size > 0:
        canvas.delete('all')
        draw_heart(canvas, x + dx, y + dy, size)
        canvas.after(10, update_heart, canvas, x, y, size, dx, dy)


# 创建一个窗口
window = tk.Tk()
window.title("Dynamic Heart")

# 创建一个画布
canvas = tk.Canvas(window, width=800, height=600, bg='white')
canvas.pack()

# 绘制心形
x, y = 400, 300
size = 200
dx, dy = 0, 0
draw_heart(canvas, x, y, size)

# 更新心形
window.after(10, update_heart, canvas, x, y, size, dx, dy)

# 运行窗口
window.mainloop()
