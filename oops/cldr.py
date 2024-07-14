import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar")
        
        self.current_year = datetime.now().year
        self.current_month = datetime.now().month

        self.header = ttk.Frame(self.root)
        self.header.pack(pady=10)

        ttk.Button(self.header, text="<", command=self.prev_month).pack(side="left")
        self.month_label = ttk.Label(self.header, text="", width=15, anchor="center")
        self.month_label.pack(side="left")
        ttk.Button(self.header, text=">", command=self.next_month).pack(side="left")

        self.calendar_frame = ttk.Frame(self.root)
        self.calendar_frame.pack()

        self.show_calendar()

    def show_calendar(self):
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()
        
        self.month_label.config(text=f"{calendar.month_name[self.current_month]} {self.current_year}")
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for day in days:
            ttk.Label(self.calendar_frame, text=day, width=5).grid(row=0, column=days.index(day))
        
        cal = calendar.monthcalendar(self.current_year, self.current_month)
        for r, week in enumerate(cal, start=1):
            for c, day in enumerate(week):
                ttk.Label(self.calendar_frame, text=day if day != 0 else "", width=5).grid(row=r, column=c)

    def prev_month(self):
        self.current_month -= 1
        if self.current_month == 0:
            self.current_month = 12
            self.current_year -= 1
        self.show_calendar()
    
    def next_month(self):
        self.current_month += 1
        if self.current_month == 13:
            self.current_month = 1
            self.current_year += 1
        self.show_calendar()

root = tk.Tk()
app = CalendarApp(root)
root.mainloop()