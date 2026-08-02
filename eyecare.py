import tkinter as tk
import time
import threading

WORK_MINUTES = 25

def popup():
    root = tk.Tk()
    root.title("Göz Molası")

    tk.Label(
        root,
        text="20 saniye boyunca uzağa bak 👀",
        font=("Arial", 16)
    ).pack(padx=30, pady=30)

    tk.Button(root, text="Tamam", command=root.destroy).pack(pady=10)

    root.mainloop()

def timer():
    while True:
        time.sleep(WORK_MINUTES * 60)
        popup()

threading.Thread(target=timer, daemon=True).start()

while True:
    time.sleep(1)
