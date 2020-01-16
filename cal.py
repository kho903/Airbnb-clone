import calendar


class Calendar():

    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.day_names = ("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")
        self.months = (
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        )

    def get_month(self):
        return self.months[self.month - 1]

