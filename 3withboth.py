import tkinter as tk
import time
import threading

root = tk.Tk()
timer = 0
count = 0
keep_ticking = True

timer_label = tk.Label(root, text=f'{timer}')
counter_label = tk.Label(root, text=f'{count}')


def tick_time():
    global timer
    while keep_ticking:
        timer += 1
        # timer_label.configure(text=f'{timer}') dit draait op een achtergrond-thread, dus dit 'mag eigenlijk niet'
        time.sleep(0.1)


def update_label():  # Dit regelt tkinter zelf, dus we splitsen het 'laat het zien in tkinter' gedeelte van het ticken
    timer_label.configure(text=f'{timer}')
    timer_label.after(10, update_label)


timer_label.after(10, update_label)


def increment_count():
    global count
    count += 1
    counter_label.configure(text=f'{count}')


increment_btn = tk.Button(root, text='++', command=increment_count)

timer_label.pack()
counter_label.pack()
increment_btn.pack()

thread = threading.Thread(target=tick_time)
thread.start()


def quit():  # omdat we background threads gebruiken moeten we alles met het handje stoppen
    global keep_ticking
    root.destroy()
    keep_ticking = False


root.protocol("WM_DELETE_WINDOW", quit)

root.mainloop()
