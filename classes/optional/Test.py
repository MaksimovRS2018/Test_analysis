from classes.optional.Date_and_time import Date_and_time


class Test:
    def __init__(self,name):
        self.number_start = None
        self.number_test = None
        self.date_and_time_test = Date_and_time()
        self.name_file = name.split(".cfg")[0]

    def parse_name(self):
        self.number_start = self.name_file.split(" ")[3]
        self.number_test = self.name_file.split(" ")[6]
        date_test_str = self.name_file.split("Time = ")[1].split(" ")[0]
        list_date_test = date_test_str.split("_")
        # костыль нужен, потому что в некоторых файлах есть еще один доп. нижнее подчеркивание
        if list_date_test[0] == "":
            list_date_test.pop(0)
        time_test_str = self.name_file.split("Time = ")[1].split(" ")[1]
        list_time_test = time_test_str.split("_")
        self.date_and_time_test.determine_date_test(list_date_test)
        self.date_and_time_test.determine_time_test(list_time_test)
