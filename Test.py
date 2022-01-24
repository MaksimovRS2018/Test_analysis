from Date_and_time import Date_and_time


class Test():
    def __init__(self):
        self.number_start = None
        self.number_test = None
        self.date_test = Date_and_time()
        self.__name_file = ""

    def determine_data_test(self, data):
        self.date_test = data

    def set_name_test_file(self, name):
        self.__name_file = name.split(".cfg")[0]
        self.parse_name()

    def parse_name(self):
        self.number_start = self.__name_file.split(" ")[3]
        self.number_test = self.__name_file.split(" ")[6]
        date_test_str = self.__name_file.split("Time = ")[1].split(" ")[0]
        list_date_test = date_test_str.split("_")
        # костыль нужен, потому что в некоторых файлах есть еще один доп. нижнее подчеркивание
        if list_date_test[0] == "":
            list_date_test.pop(0)
        time_test_str = self.__name_file.split("Time = ")[1].split(" ")[1]
        list_time_test = time_test_str.split("_")
        self.date_test.determine_date_test(list_date_test)
        self.date_test.determine_date_test(list_time_test)
