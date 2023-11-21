class DateUtilities:

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def day_month_starts(month, year):
        if month < 3:
            month += 12
            year -= 1

        k = year % 100
        j = year // 100

     
        f = 1  
        h = (f + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) + (5 * j)) % 7

        day_of_week = (h + 6) % 7

        return day_of_week

    @staticmethod
    def days_in_month(month, year):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 12 or month == 10:
            number_days = 31

        elif month == 4 or month == 6 or month == 9 or month == 11:
            number_days = 30
        else:

            leap_year = DateUtilities.is_leap_year(year)
            if leap_year:
                number_days = 29
            else:
                number_days = 28
        return number_days
