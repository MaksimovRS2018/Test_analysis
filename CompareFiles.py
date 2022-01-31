import os
from datetime import datetime
from shutil import copyfile
from Test import Test
from datetime import timedelta

path_RTDS = "D:\\YandexDisk\\Test2\\KSZ"
path_terminal = "D:\\YandexDisk\\Test\\KSZ 500\\Terminals\\"
path_dst_start = "D:\\rtds_test\\tests\\"


def copy_rtds_files_to_dst_and_get_dst(path_start, test_rtds, max_number):
    flag = True
    path = path_start
    while flag or max_number > -1:
        try:
            number_test_split = test_rtds.number_test.split(".")
            if len(number_test_split) > max_number:
                number_test_split = number_test_split[:max_number]
            new_folder = ""
            for k in range(len(number_test_split)):
                new_folder = new_folder + test_rtds.number_test.split(".")[k] + "."
                path = path + new_folder + "\\"
            flag = False
            copyfile(path_RTDS + "\\" + test_rtds.name_file + ".cfg", path + test_rtds.name_file + " RTDS " + ".cfg")
            copyfile(path_RTDS + "\\" + test_rtds.name_file + ".dat", path + test_rtds.name_file + " RTDS " + ".dat")
            copyfile(path_RTDS + "\\" + test_rtds.name_file + ".pdf", path + test_rtds.name_file + " RTDS " + ".pdf")
            return path
        except FileNotFoundError:
            max_number = max_number - 1
    return None


def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.fromtimestamp(t)


def copy_terminal_files_to_dst(path_oscill_terminal, path_dst, test_rtds, substation):
    try:
        list_name_files_oscill_terminal = os.listdir(path_oscill_terminal)
        time_creating_comtrade_file = modification_date(
            path_oscill_terminal + "\\" + list_name_files_oscill_terminal[0])
        copyfile(path_oscill_terminal + "\\" + list_name_files_oscill_terminal[0],
                 path_dst + test.name_file + " Terminal " + substation + " "
                 + list_name_files_oscill_terminal[0])
        copyfile(path_oscill_terminal + "\\" + list_name_files_oscill_terminal[1],
                 path_dst + test.name_file + " Terminal " + substation + " "
                 + list_name_files_oscill_terminal[1])
        return time_creating_comtrade_file
    except FileNotFoundError:
        f.write(
            "Нет осциллогаммы терминала на  " + substation + " для опыта " + test_rtds.number_test
            + " c пуском №" + test_rtds.number_start +
            ". Имя файла осциллограммы RTDS: " + test_rtds.name_file + "\n")


def compare_files(test_rtds, time, flag_compare):
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
                                f.write("Сбита нумерация опытов, начиная с " + test_rtds.number_start + "\n")
                                return False
        return True


def filter_list_files(all_files):
    # фильтрация по общему началу
    files_only_test = list(filter(lambda x: x.find("Number start") != -1, all_files))
    # фильтрация по 1 типу, остальные нет смысла проходить(dat,pdf)
    files_only_ony_type = list(filter(lambda x: x.find(".cfg") != -1, files_only_test))
    return files_only_ony_type


flag_compare_SUBA = True
flag_compare_SUBB = True
list_name_FilesOrDir = os.listdir(path_RTDS)
list_name_FilesOrDir.sort()
actual_time = datetime.utcnow() + timedelta(hours=3)
data_now = str(actual_time).split(" ")[0]
time_now = str(actual_time).split(" ")[1]
name_log_file = "log" + data_now + ".log"
with open(name_log_file, "a", encoding='utf-8') as f:
    f.write(
        "===============================" + data_now
        + time_now + "=========================================================\n")
    test_files = filter_list_files(list_name_FilesOrDir)
    print("Всего опытов = ", len(test_files))

    for one_File in range(len(test_files)):
        test = Test(test_files[one_File])
        test.parse_name()
        path_oscill_terminal_SUBA = path_terminal + test.date_and_time_test.date_test.year_test + "_" \
                                    + test.date_and_time_test.date_test.month_test + "_" \
                                    + test.date_and_time_test.date_test.day_test \
                                    + "\\ЭКРА1\\Присоединение 500кВ\\КСЗ ПСА\\Пуск " \
                                    + test.number_start.rjust(3, '0')
        path_oscill_terminal_SUBB = path_terminal + test.date_and_time_test.date_test.year_test + "_" \
                                    + test.date_and_time_test.date_test.month_test + "_" \
                                    + test.date_and_time_test.date_test.day_test \
                                    + "\\ЭКРА1\\Присоединение 500кВ\\КСЗ ПСБ\\Пуск " \
                                    + test.number_start.rjust(3, '0')
        path_dst = copy_rtds_files_to_dst_and_get_dst(path_start=path_dst_start, test_rtds=test, max_number=3)

        if path_dst is not None:
            if flag_compare_SUBA:
                time_creating_comtrade_file_SUBA = copy_terminal_files_to_dst(path_oscill_terminal_SUBA, path_dst,
                                                                              test,
                                                                              "ПСА")
                flag_compare_SUBA = compare_files(test, time_creating_comtrade_file_SUBA, flag_compare_SUBA)
            if flag_compare_SUBB:
                time_creating_comtrade_file_SUBB = copy_terminal_files_to_dst(path_oscill_terminal_SUBB, path_dst,
                                                                              test,
                                                                              "ПСБ")
                flag_compare_SUBB = compare_files(test, time_creating_comtrade_file_SUBA, flag_compare_SUBB)
        else:
            f.write("Ошибка в копировании файла " + test.name_file)

        print('Выполнено = ' + str(((one_File+1) / len(test_files)) * 100) + " % ")
f.close()
