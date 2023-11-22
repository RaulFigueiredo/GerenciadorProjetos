from datetime import date

class MonthYearNavigation:
    def __init__(self, navigation_frame, button_back, label_month_year, button_forward, update_callback):
        self.navigation_frame = navigation_frame
        self.button_back = button_back
        self.label_month_year = label_month_year
        self.button_forward = button_forward
        self.update_callback = update_callback
        self.month = date.today().month
        self.year = date.today().year

        self.button_back.configure(command=lambda: self.update_display(*self.change_month(-1)))
        self.button_forward.configure(command=lambda: self.update_display(*self.change_month(1)))
        self.update_display(self.month, self.year)
        
    def update_display(self, month, year):
        months = ["January", "February", "March", "April", "May", "June", 
                  "July", "August", "September", "October", "November", "December"]
        written_month = months[month - 1]
        self.label_month_year.config(text=f"{written_month} {year}")
        self.update_callback(month, year)

        return written_month, year

    def change_month(self, direction):
        self.month += direction
        if self.month > 12:
            self.month = 1
            self.year += 1
        elif self.month < 1:
            self.month = 12
            self.year -= 1
        return self.month, self.year