import customtkinter
import time
#--------------------------
customtkinter.set_appearance_mode("dark")
#--------------------------
CLOCK_FONT = ("Comic Sans MS", 40)
DATE_FONT = ("Comic Sans MS", 27)

#--------------------------
class ClockApp:
    def __init__(self, windows):
        self.windows = windows

        self.clock_label = customtkinter.CTkLabel(self.windows, text="00:00:00", font =CLOCK_FONT)
        self.clock_label.pack(padx=15, pady=15)

        self.date_label = customtkinter.CTkLabel(self.windows, text="Thursday, January 1, 1970",font =DATE_FONT)
        self.date_label.pack(padx=15, pady=15)
        self.update()
    def update(self):
        clock_time = time.strftime("%H:%M:%S")
        date_time = time.strftime("%A, %B %d, %Y")
        self.clock_label.configure(text=clock_time)
        self.date_label.configure(text=date_time)
        self.windows.after(1000, self.update)











if __name__ == "__main__":
    windows = customtkinter.CTk()
    app = ClockApp(windows)
    windows.title("Clock")
    windows.mainloop()
    