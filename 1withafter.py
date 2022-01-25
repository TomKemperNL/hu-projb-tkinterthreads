import tkinter as tk
import time

root = tk.Tk()
timer = 0
count = 0

timer_label = tk.Label(root, text=f'{timer}')
counter_label = tk.Label(root, text=f'{count}')


def tick_time():
    global timer
    timer += 1
    time.sleep(1)  # Dit hier is het probleem, langdurende operaties
    timer_label.configure(text=f'{timer}')
    root.after(10, tick_time)
    timer_label.forget()
    timer_label.pack()


def increment_count():
    global count
    count += 1
    counter_label.configure(text=f'{count}')


increment_btn = tk.Button(root, text='++', command=increment_count)

timer_label.pack()
counter_label.pack()
increment_btn.pack()
root.after(10, tick_time)
root.mainloop()
