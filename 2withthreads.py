import tkinter as tk
import time
import threading

root = tk.Tk()
timer = 0
count = 0

timer_label = tk.Label(root, text=f'{timer}')
counter_label = tk.Label(root, text=f'{count}')


def tick_time():
    global timer
    while True:
        timer += 1
        timer_label.configure(text=f'{timer}')
        time.sleep(0.1)


def increment_count():
    global count
    count += 1
    counter_label.configure(text=f'{count}')


increment_btn = tk.Button(root, text='++', command=increment_count)

timer_label.pack()
counter_label.pack()
increment_btn.pack()

thread = threading.Thread(target=tick_time) # In plaats van root.after(tick_time) maken we hier iets dat een Thread heet
thread.start()
root.mainloop()

# Dit werkt, maar gooit een error bij het afsluiten:
# RuntimeError: main thread is not in main loop
# Dat is zorgwekkend, en hoewel ik het hier niet kan nabouwen kan dit ook op vervelendere momenten voorkomen dan bij
# het afsluiten:
# Bron: https://stackoverflow.com/questions/64287940/update-tkinter-gui-from-a-separate-thread-running-a-command
