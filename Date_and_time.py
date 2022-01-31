class Date_test:
    def __init__(self):
        self.year_test = None
        self.month_test = None
        self.day_test = None


class Time_test:
    def __init__(self):
        self.hour_test = None
        self.minute_test = None
        self.second_test = None

class Date_and_time:
    def __init__(self):
        self.date_test = Date_test()
        self.time_test = Time_test()

    def determine_date_test(self, date):
        self.date_test.day_test = date[1]
        self.date_test.month_test = date[0]
        self.date_test.year_test = date[2]

    def determine_time_test(self, time):
        self.time_test.hour_test = time[0]
        self.time_test.minute_test = time[1]
        self.time_test.second_test = time[2]
