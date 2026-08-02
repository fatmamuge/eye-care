import tkinter as tk

WORK_MINUTES = 25
INTERVAL_MS = int(WORK_MINUTES * 60 * 1000)


class EyeCare:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Ana pencereyi gizle

        self.popup_open = False

        # İlk zamanlayıcı
        self.start_timer()

        self.root.mainloop()

    def start_timer(self):
        self.root.after(INTERVAL_MS, self.show_popup)

    def show_popup(self):
        print("show_popup() called")

        # Eğer pencere zaten açıksa yenisini açma
        if self.popup_open:
            return

        self.popup_open = True

        popup = tk.Toplevel(self.root)
        popup.title("👀 EyeCare")

        popup.geometry("360x180")
        popup.resizable(False, False)

        tk.Label(
            popup,
            text="👀 Eye Break Time!",
            font=("Arial", 16, "bold")
        ).pack(pady=(20, 10))

        tk.Label(
            popup,
            text="Look at something far away\nfor 20 seconds.",
            font=("Arial", 12)
        ).pack()

        def close_popup():
            self.popup_open = False
            popup.destroy()

            # Pencere kapandıktan sonra yeni sayaç başlasın
            self.start_timer()

        tk.Button(
            popup,
            text="OK",
            command=close_popup,
            width=10
        ).pack(pady=20)

        popup.protocol("WM_DELETE_WINDOW", close_popup)


if __name__ == "__main__":
    EyeCare()
