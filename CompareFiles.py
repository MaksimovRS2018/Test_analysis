path_RTDS = "D:\\YandexDisk\\Test2\\KSZ"
path_terminal = "D:\\YandexDisk\\Test\\KSZ 500\\Terminals\\"
import os
from datetime import datetime
from shutil import copyfile

from datetime import timedelta

# def copy_rtds_files_to_dir(max_number):
#     try:
#         number_test_split = number_test.split(".")
#         if len(number_test_split) > max_number:
#             number_test_split = number_test_split[:max_number]
#         path_dst = "C:\\Users\\maksi\\PycharmProjects\\for_tests\\tests\\"
#         new_folder = ""
#         for k in range(len(number_test_split)):
#             new_folder = new_folder + number_test.split(".")[k] + "."
#             path_dst = path_dst + new_folder + "\\"
#
#         copyfile(path_RTDS + "\\" + test + ".cfg", path_dst + test + " RTDS " + ".cfg")
#         copyfile(path_RTDS + "\\" + test + ".dat", path_dst + test + " RTDS " + ".dat")
#         copyfile(path_RTDS + "\\" + test + ".pdf", path_dst + test + " RTDS " + ".pdf")
#         return False, path_dst
#     except FileNotFoundError:
#         return True, None



path_dst = "C:\\Users\\maksi\\PycharmProjects\\for_tests\\tests\\"
list_name_FilesOrDir = os.listdir(path_RTDS)
list_name_FilesOrDir.sort()
actual_time = datetime.utcnow() + timedelta(hours=3)
data_now = str(actual_time).split(" ")[0]
time_now = str(actual_time).split(" ")[1]
name_log_file = "log" + data_now + ".txt"
with open(name_log_file, "a", encoding='utf-8') as f:
    f.write("=============================== %s %s + =========================================================\n",data_now,time_now)
f.close()
# for name_FileOrDir in range(len(list_name_FilesOrDir)):
#     print(list_name_FilesOrDir[name_FileOrDir])
#     # фильтрация по общему началу
#     if list_name_FilesOrDir[name_FileOrDir].find("Number start") != -1:
#         # фильтрация по 1 типу, остальные нет смысла проходить(dat,pdf)
#         if list_name_FilesOrDir[name_FileOrDir].find(".cfg") != -1:
#             test = list_name_FilesOrDir[name_FileOrDir].split(".cfg")[0]
#             number_start = test.split(" ")[3]
#             number_test = test.split(" ")[6]
#             data_test = test.split("Time = ")[1].split(" ")[0]
#             list_pars_datetime = data_test.split("_")
#             # костыль нужен, потому что в некоторых файлах есть еще один доп. нижнее подчеркивание
#             if list_pars_datetime[0] == "":
#                 day = data_test.split("_")[2]
#                 month = data_test.split("_")[1]
#                 year = data_test.split("_")[3]
#             else:
#                 day = data_test.split("_")[1]
#                 month = data_test.split("_")[0]
#                 year = data_test.split("_")[2]
#             time_test = test.split("Time = ")[1].split(" ")[1]
#             print(data_test)
#             hour = time_test.split("_")[0]
#             minute = time_test.split("_")[1]
#             second = str(int(float(time_test.split("_")[2])))
#             print(time_test)
#             path_oscill_terminal_SUBA = path_terminal + year + "_" + month + "_" + day + "\\ЭКРА1\\Присоединение 500кВ\\КСЗ ПСА\\Пуск " + number_start.rjust(
#                 3, '0')
#             path_oscill_terminal_SUBB = path_terminal + year + "_" + month + "_" + day + "\\ЭКРА1\\Присоединение 500кВ\\КСЗ ПСБ\\Пуск " + number_start.rjust(
#                 3, '0')
#
#             flag = True
#             max_number = 3
#             while(flag):
#                 flag,path_dst = copy_rtds_files_to_dir(max_number)
#                 if flag:
#                     max_number = max_number - 1
#
#
#
#             with open(name_log_file, "a", encoding='utf-8') as f:
#                 try:
#                     list_name_files_oscill_terminal_SUBA = os.listdir(path_oscill_terminal_SUBA)
#                     pathhhh = path_dst + test + " Terminal SUBA "  + list_name_files_oscill_terminal_SUBA[0]
#                     copyfile(path_oscill_terminal_SUBA + "\\" + list_name_files_oscill_terminal_SUBA[0], path_dst + test + " Terminal SUBA "  + list_name_files_oscill_terminal_SUBA[0])
#                     copyfile(path_oscill_terminal_SUBA + "\\" + list_name_files_oscill_terminal_SUBA[1], path_dst + test + " Terminal SUBA " + list_name_files_oscill_terminal_SUBA[1])
#                     # f.write( "Есть осциллогаммы терминала для опыта " + number_test + " c пуском №" + number_start + ". Имя файла осциллограммы RTDS: " + test + "\n")
#                 except FileNotFoundError:
#                     f.write(
#                         "Нет осциллогаммы терминала на ПСА для опыта " + number_test + " c пуском №" + number_start +
#                         ". Имя файла осциллограммы RTDS: " + test + "\n")
#                 try:
#                     list_name_files_oscill_terminal_SUBB = os.listdir(path_oscill_terminal_SUBB)
#                     copyfile(path_oscill_terminal_SUBB + "\\" + list_name_files_oscill_terminal_SUBB[0], path_dst + test + " Terminal SUBB " + list_name_files_oscill_terminal_SUBB[0])
#                     copyfile(path_oscill_terminal_SUBB + "\\" + list_name_files_oscill_terminal_SUBB[1], path_dst + test + " Terminal SUBB " + list_name_files_oscill_terminal_SUBB[1])
#                     # f.write( "Есть осциллогаммы терминала для опыта " + number_test + " c пуском №" + number_start + ". Имя файла осциллограммы RTDS: " + test + "\n")
#                 except FileNotFoundError:
#                     f.write(
#                         "Нет осциллогаммы терминала на ПСБ для опыта " + number_test + " c пуском №" + number_start +
#                         ". Имя файла осциллограммы RTDS: " + test + "\n")
#                 f.close()


