import tkinter as tk
from pynput import keyboard
from collections import deque

# Параметры отображения — можно сделать настраиваемыми через конфиг
FONT = ("JetBrainsMono Nerd Font", 32, "bold")
BG_COLOR = "#222222"
FG_COLOR = "#FFFFFF"
WINDOW_OPACITY = 0.9 # 90% прозрачности (10% непрозрачности)
MAX_KEYS = 6

# Очередь последних клавиш
key_buffer = deque(maxlen=MAX_KEYS)

# Создание окна
root = tk.Tk()
root.title("Key Display")
root.configure(bg=BG_COLOR)
root.attributes("-topmost", True)
root.attributes("-alpha", WINDOW_OPACITY) # Делаем все окно полупрозрачным
# root.attributes("-transparentcolor", BG_COLOR) # Удалено, так как больше не требуется
root.geometry("300x100+500+300")  # Сдвиг окна
root.overrideredirect(True)  # Без рамки

# Метка для вывода клавиш
label = tk.Label(root, text="", font=FONT, bg=BG_COLOR, fg=FG_COLOR)
label.pack(expand=True, fill="both")

# Перетаскивание окна
def start_drag(event):
    root._x = event.x
    root._y = event.y

def do_drag(event):
    x = root.winfo_x() + event.x - root._x
    y = root.winfo_y() + event.y - root._y
    root.geometry(f"300x100+{x}+{y}") # Обновляем размер окна при перетаскивании

def stop_drag(event):
    pass # Ничего не делаем при отпускании кнопки, но можно добавить логику, если потребуется

root.bind("<Button-3>", start_drag)
root.bind("<B3-Motion>", do_drag)
root.bind("<ButtonRelease-3>", stop_drag)

# Обработка нажатия клавиш
def on_press(key):
    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key).replace("Key.", "").upper()

    key_buffer.append(key_str)
    label.config(text="  ".join(key_buffer))

# Слушатель клавиатуры
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Запуск окна
root.mainloop()