import os
import logging
from datetime import datetime
from shutil import copyfile
from Test import Test
from tqdm import tqdm
from datetime import timedelta


class ComparatorFiles:
    def __init__(self, logger=logging.getLogger("None"), path_to_RTDS="", path_to_terminal="", path_to_test_folders=""):
        self.logger = logger
        self.path_to_RTDS = path_to_RTDS
        self.path_to_terminal = path_to_terminal
        self.path_to_test_folders = path_to_test_folders

    def __copy_rtds_files_to_dst_and_get_dst(self, path_start, test_rtds, max_number):
        flag = True

        while flag or max_number > -1:

            try:
                path = path_start
                number_test_split = test_rtds.number_test.split(".")
                if len(number_test_split) > max_number:
                    number_test_split = number_test_split[:max_number]
                new_folder = ""
                for k in range(len(number_test_split)):
                    new_folder = new_folder + test_rtds.number_test.split(".")[k] + "."
                    path = path + new_folder + "\\"
                flag = False
                copyfile(self.path_to_RTDS + "\\" + test_rtds.name_file + ".cfg",
                         path + test_rtds.name_file + " RTDS " + ".cfg")
                copyfile(self.path_to_RTDS + "\\" + test_rtds.name_file + ".dat",
                         path + test_rtds.name_file + " RTDS " + ".dat")
                copyfile(self.path_to_RTDS + "\\" + test_rtds.name_file + ".pdf",
                         path + test_rtds.name_file + " RTDS " + ".pdf")
                return path
            except FileNotFoundError:
                max_number = max_number - 1
        return None

    def __modification_date(self, filename):
        t = os.path.getmtime(filename)
        return datetime.fromtimestamp(t)

    def __copy_terminal_files_to_dst(self, path_oscill_terminal, path_dst, test_rtds, substation):
        try:
            list_name_files_oscill_terminal = os.listdir(path_oscill_terminal)
            time_creating_comtrade_file = self.__modification_date(
                path_oscill_terminal + "\\" + list_name_files_oscill_terminal[0])
            copyfile(path_oscill_terminal + "\\" + list_name_files_oscill_terminal[0],
                     path_dst + test_rtds.name_file + " Terminal " + substation + " "
                     + list_name_files_oscill_terminal[0])
            copyfile(path_oscill_terminal + "\\" + list_name_files_oscill_terminal[1],
                     path_dst + test_rtds.name_file + " Terminal " + substation + " "
                     + list_name_files_oscill_terminal[1])
            return time_creating_comtrade_file
        except FileNotFoundError:
            self.logger.warning(
                f"Нет осциллогаммы терминала на  {substation} для опыта {test_rtds.number_test}" +
                f" c пуском №{test_rtds.number_start}. " +
                f"Имя файла осциллограммы RTDS: {test_rtds.name_file}"
            )

    def __compare_files(self, test_rtds, time, flag_compare):
        delta = 10
        if flag_compare:
            if int(test_rtds.date_and_time_test.date_test.year_test) == int(time.year):
                if int(test_rtds.date_and_time_test.date_test.month_test) == int(time.month):
                    if int(test_rtds.date_and_time_test.date_test.day_test) == int(time.day):
                        if int(test_rtds.date_and_time_test.time_test.hour_test) == int(time.time().hour):
                            if int(test_rtds.date_and_time_test.time_test.minute_test) == int(time.time().minute):
                                if not (int(time.time().second - delta)
                                        <= int(float(test_rtds.date_and_time_test.time_test.second_test)) \
                                        <= int(time.time().second + delta)):
                                    self.logger.warning(f"Сбита нумерация опытов, начиная с {test_rtds.number_start}")
                                    return False
            return True

    def __filter_list_files(self, all_files):
        # фильтрация по общему началу
        files_only_test = list(filter(lambda x: x.find("Number start") != -1, all_files))
        # фильтрация по 1 типу, остальные нет смысла проходить(dat,pdf)
        files_only_ony_type = list(filter(lambda x: x.find(".cfg") != -1, files_only_test))
        return files_only_ony_type

    def start(self):
        self.logger.info("Comparator start")
        flag_compare_SUBA = True
        flag_compare_SUBB = True
        list_name_FilesOrDir = os.listdir(self.path_to_RTDS)
        list_name_FilesOrDir.sort()

        test_files = self.__filter_list_files(list_name_FilesOrDir)

        for iter_file_test in tqdm(range(len(test_files))):
            test = Test(test_files[iter_file_test])
            test.parse_name()
            path_oscill_terminal_SUBA = self.path_to_terminal + test.date_and_time_test.date_test.year_test + "_" \
                                        + test.date_and_time_test.date_test.month_test + "_" \
                                        + test.date_and_time_test.date_test.day_test \
                                        + "\\ЭКРА1\\Присоединение 500кВ\\КСЗ ПСА\\Пуск " \
                                        + test.number_start.rjust(3, '0')
            path_oscill_terminal_SUBB = self.path_to_terminal + test.date_and_time_test.date_test.year_test + "_" \
                                        + test.date_and_time_test.date_test.month_test + "_" \
                                        + test.date_and_time_test.date_test.day_test \
                                        + "\\ЭКРА1\\Присоединение 500кВ\\КСЗ ПСБ\\Пуск " \
                                        + test.number_start.rjust(3, '0')
            path_dst = self.__copy_rtds_files_to_dst_and_get_dst(path_start=self.path_to_test_folders, test_rtds=test,
                                                               max_number=3)

            if path_dst is not None:
                if flag_compare_SUBA:
                    time_creating_comtrade_file_SUBA = self.__copy_terminal_files_to_dst(path_oscill_terminal_SUBA,
                                                                                       path_dst,
                                                                                       test,
                                                                                       "ПСА")
                    flag_compare_SUBA = self.__compare_files(test, time_creating_comtrade_file_SUBA, flag_compare_SUBA)
                if flag_compare_SUBB:
                    time_creating_comtrade_file_SUBB = self.__copy_terminal_files_to_dst(path_oscill_terminal_SUBB,
                                                                                       path_dst,
                                                                                       test,
                                                                                       "ПСБ")
                    flag_compare_SUBB = self.__compare_files(test, time_creating_comtrade_file_SUBB, flag_compare_SUBB)
            else:
                self.logger.warning(f"Ошибка в копировании файла {test.name_file}")

        self.logger.info("Comparator finish")
