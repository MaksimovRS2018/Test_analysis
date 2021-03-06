from classes.optional.Parser_comtrade import Parser_comtrade
import numpy as np
import os
from tqdm import tqdm


class Writer_info_in_report:

    def __init__(self, logger, path_to_tests="", condition=False):
        self.logger = logger
        self.path_report = path_to_tests + "\\report.txt"
        self.path_to_test = path_to_tests
        self.condition = condition

        self.list_signals_from_rtds_sub_a = ["TRIP_DZ_1_st_SUB_A", "TRIP_DZ0_1_st_SUB_A", "TRIP_DZ_2_st_SUB_A",
                                             "TRIP_DZ_3_st_SUB_A",
                                             "TRIP_TNZNP_1_st_SUB_A", "TRIP_TNZNP_2_st_SUB_A", "TRIP_TNZNP_3_st_SUB_A",
                                             "TRIP_phA_SUB_A", "TRIP_phB_SUB_A", "TRIP_phC_SUB_A", "OTF_SUB_A",
                                             "SEND_VCH2_SUB_A",
                                             "TRIP_BNN_A"]
        self.list_signals_from_rtds_sub_b = ["TRIP_DZ_1_st_SUB_B", "TRIP_DZ0_1_st_SUB_B", "TRIP_DZ0_1_st_SUB_B",
                                             "TRIP_DZ_3_st_SUB_B",
                                             "TRIP_TNZNP_1_st_SUB_B", "TRIP_TNZNP_2_st_SUB_B", "TRIP_TNZNP_3_st_SUB_B",
                                             "TRIP_phA_SUB_B", "TRIP_phB_SUB_B", "TRIP_phC_SUB_B", "OTF_SUB_B",
                                             "SEND_VCH2_SUB_B"]
        self.list_signals_from_terminal = [
            "1 ИО Z Iст.AB", "2 ИО Z Iст.BC", "3 ИО Z Iст.CA",
            "4 ИО Z IIст.АВ", "5 ИО Z IIст.BC", "6 ИО Z IIст.CA",
            "7 ИО Z IIIст.АВ", "8 ИО Z IIIст.BC", "9 ИО Z IIIст.CA",
            "16 ИО Z ABC IIст.",
            "17 ИО Z Iст.АN", "18 ИО Z Iст.BN", "19 ИО Z Iст.CN",
            "26 ПО Io Iст.", "27 ПО Io IIст.", "28 ПО Io IIIст.",
            "300 Сраб.ИПФ А",
            "301 Сраб.ИПФ В",
            "302 Сраб.ИПФ С"
        ]

        self.list_flt = ["FLT1", "FLT2", "FLT3", "FLT4", "FLT5", "FLT6", "FLT7", "FLT8", "FLT9", "FLT1.1", "FLT1.2",
                         "FLT1.3"]
        self.list_flt_int = ["FLT1", "FLT5", "FLT1.1", "FLT1.2", "FLT1.3"]
        self.list_flt_ext = ["FLT2", "FLT3", "FLT4", "FLT6", "FLT7", "FLT8", "FLT9"]

        self.dictionary = {
            'TRIP_DZ_1_st_SUB_A': "Срабатывание ДЗ 1 ст. на ПСА ",
            'TRIP_DZ0_1_st_SUB_A': "Срабатывание ДЗ 1 ст. ф.к. на ПСА ",
            'TRIP_DZ_2_st_SUB_A': "Срабатывание ДЗ 2 ст. на ПСА ",
            'TRIP_DZ_3_st_SUB_A': "Срабатывание ДЗ 3 ст. на ПСА ",
            'TRIP_TNZNP_1_st_SUB_A': "Срабатывание ТНЗНП 1 ст. на ПСА ",
            'TRIP_TNZNP_2_st_SUB_A': "Срабатывание ТНЗНП 2 ст. на ПСА ",
            'TRIP_TNZNP_3_st_SUB_A': "Срабатывание ТНЗНП 3 ст. на ПСА ",
            'TRIP_phA_SUB_A': "Отключение ф.А выключателя на ПСА ",
            'TRIP_phB_SUB_A': "Отключение ф.B выключателя на ПСА ",
            'TRIP_phC_SUB_A': "Отключение ф.C выключателя на ПСА ",
            'OTF_SUB_A': "Отключение 3-х фаз выключателя на ПСА ",
            'SEND_VCH2_SUB_A': "Отправка высокочастотного сигнала отключения 3-х фаз с ПСА на ПСБ ",
            'TRIP_DZ_1_st_SUB_B': "Срабатывание ДЗ 1 ст. на ПСБ ",
            'TRIP_DZ0_1_st_SUB_B': "Срабатывание ДЗ 1 ст. ф.к. на ПСБ ",
            'TRIP_DZ_2_st_SUB_B': "Срабатывание ДЗ 2 ст. на ПСБ ",
            'TRIP_DZ_3_st_SUB_B': "Срабатывание ДЗ 3 ст. на ПСБ ",
            'TRIP_TNZNP_1_st_SUB_B': "Срабатывание ТНЗНП 1 ст. на ПСБ ",
            'TRIP_TNZNP_2_st_SUB_B': "Срабатывание ТНЗНП 2 ст. на ПСБ ",
            'TRIP_TNZNP_3_st_SUB_B': "Срабатывание ТНЗНП 3 ст. на ПСБ ",
            'TRIP_phA_SUB_B': "Отключение ф.А выключателя на ПСБ ",
            'TRIP_phB_SUB_B': "Отключение ф.B выключателя на ПСБ ",
            'TRIP_phC_SUB_B': "Отключение ф.C выключателя на ПСБ ",
            'OTF_SUB_B': "Отключение 3-х фаз выключателя на ПСБ ",
            'SEND_VCH2_SUB_B': "Отправка высокочастотного сигнала отключения 3-х фаз с ПСБ на ПСА ",
            "1 ИО Z Iст.AB": "Пуск 1 ст. ДЗ мф.к. AB ",
            "2 ИО Z Iст.BC": "Пуск 1 ст. ДЗ мф.к. BC ",
            "3 ИО Z Iст.CA": "Пуск 1 ст. ДЗ мф.к. CA ",
            "4 ИО Z IIст.АВ": "Пуск 2 ст. ДЗ мф.к. AB ",
            "5 ИО Z IIст.BC": "Пуск 2 ст. ДЗ мф.к. BC ",
            "6 ИО Z IIст.CA": "Пуск 2 ст. ДЗ мф.к. CA ",
            "7 ИО Z IIIст.АВ": "Пуск 3 ст. ДЗ мф.к. АВ ",
            "8 ИО Z IIIст.BC": "Пуск 3 ст. ДЗ мф.к. BC ",
            "9 ИО Z IIIст.CA": "Пуск 3 ст. ДЗ мф.к. CA ",
            "16 ИО Z ABC IIст.": "Пуск 2 ст. ДЗ ABC ",
            "17 ИО Z Iст.АN": "Пуск 1 ст. ДЗ ф.к. АN ",
            "18 ИО Z Iст.BN": "Пуск 1 ст. ДЗ ф.к. BN ",
            "19 ИО Z Iст.CN": "Пуск 1 ст. ДЗ ф.к. СN ",
            "26 ПО Io Iст.": "Пуск 1 ст. ТНЗНП ",
            "27 ПО Io IIст.": "Пуск 2 ст. ТНЗНП ",
            "28 ПО Io IIIст.": "Пуск 3 ст. ТНЗНП ",
            "300 Сраб.ИПФ А": "Срабатывание избирателя поврежденной фазы ф. А ",
            "301 Сраб.ИПФ В": "Срабатывание избирателя поврежденной фазы ф. B ",
            "302 Сраб.ИПФ С": "Срабатывание избирателя поврежденной фазы ф. С "
        }

    def __get_info(self, list_name_signals, parser_comtrade):
        indexes_trips_in_dat = []
        trips_in_test = []
        indexes_signals = []
        for name_signal in list_name_signals:
            try:
                indexes_signals.append(parser_comtrade.name_digital.index(name_signal) + 1)
            except ValueError:
                # в случае если на графиках нет какого-то сигнала
                continue
        for index_signal in range(len(indexes_signals)):
            list_data_signal = list(
                parser_comtrade.matrix_digital[:, indexes_signals[index_signal]])
            try:
                index_start_time = list_data_signal.index(1)
                indexes_trips_in_dat.append(index_start_time)
                trips_in_test.append(list_name_signals[index_signal])
            except ValueError:
                continue

        times_trips = list(map(lambda x: parser_comtrade.times[x] / 1000000, indexes_trips_in_dat))
        return trips_in_test, times_trips

    def __analyze_oscill(self, list_trip_sub, list_time_trip_sub, flts_in_test, times_start_flt, name_sub, brk):
        text = ""
        if len(flts_in_test) >= 1:  # если в опыте есть КЗ
            if len(flts_in_test) == 1:  # если в опыте одно КЗ
                if len(list_trip_sub) == 0:  # если отсутствуют срабатывания при наличии кз
                    text = text + "5 / Отсутствие срабатывания защиты на " + name_sub + '\n'
                    if flts_in_test[0] in self.list_flt_int:  # если кз внутренеее и нет срабатывания
                        if brk == 1:
                            text = text + "5 / Отказ срабатывания защиты на " + name_sub + '\n'
                else:  # если есть срабатывания при наличии кз
                    if flts_in_test[0] in self.list_flt_ext:  # если кз внешнее
                        text = text + "5 / Излишнее срабатывания защиты на " + name_sub + '\n'
                    for trip_prot_one_sub in range(len(list_trip_sub)):
                        text = text + "5 / " + self.dictionary[list_trip_sub[trip_prot_one_sub]] + " : " + \
                               str(np.round(list_time_trip_sub[trip_prot_one_sub] - min(times_start_flt),
                                            decimals=5)) + ' c \n'
            else:  # если в опыте больше, чем одно КЗ
                if len(list_trip_sub) == 0:  # если отсутствуют срабатывания при наличии двух кз
                    text = text + "5 / Отсутствие срабатывания защиты на " + name_sub + '\n'
                else:  # если есть срабатывания при наличии двух кз
                    min_trip_prot = np.min(list_time_trip_sub)
                    min_time_flt = np.min(times_start_flt)
                    max_time_flt = np.max(times_start_flt)
                    index_min_time_flt = times_start_flt.index(min_time_flt)
                    index_max_time_flt = times_start_flt.index(max_time_flt)
                    first_flt = flts_in_test[index_min_time_flt]
                    second_flt = flts_in_test[index_max_time_flt]
                    if (first_flt in self.list_flt_ext) and (second_flt in self.list_flt_int):
                        if max_time_flt >= min_trip_prot >= min_time_flt:
                            text = text + "5 / Излишнее срабатывания защиты на " + name_sub + '\n'
                        if min_trip_prot >= max_time_flt:
                            for trip_prot_one_sub in range(len(list_trip_sub)):
                                text = text + "5 / " + self.dictionary[list_trip_sub[trip_prot_one_sub]] + " : " + \
                                       str(np.round(list_time_trip_sub[trip_prot_one_sub] - min(times_start_flt),
                                                    decimals=5)) + ' c \n'
                    if (first_flt in self.list_flt_int) and (second_flt in self.list_flt_int):
                        if min_trip_prot >= min_time_flt:
                            for trip_prot_one_sub in range(len(list_trip_sub)):
                                text = text + "5 / " + self.dictionary[list_trip_sub[trip_prot_one_sub]] + " : " + \
                                       str(np.round(list_time_trip_sub[trip_prot_one_sub] - min(times_start_flt),
                                                    decimals=5)) + ' c \n'
        else:  # если в опыте нет КЗ
            if len(list_trip_sub) == 1:  # если есть срабатывания при наличии кз
                text = text + "5 / Ложное срабатывание защиты на " + name_sub + '\n'
            else:
                text = text + "5 / Отсутствие срабатывания защиты на " + name_sub + '\n'

        return text

    def __search_all_files(self, path_to_folder):
        directory = os.walk(path_to_folder)
        all_path_and_files = []
        all_actual_namefiles = []
        # TODO упростить
        for d in directory:
            if len(d[len(d) - 1]) != 0:
                one = []
                one.append(d[0])
                one.append(d[2])
                all_path_and_files.append(one)
        for i in range(len(all_path_and_files)):
            # print(all_path_and_files[i])
            path_folder = all_path_and_files[i][0]
            for path in all_path_and_files[i][1]:
                full_path = path_folder + "\\" + path
                if full_path.find(".cfg") != -1:
                    all_actual_namefiles.append(full_path.split(".cfg")[0])
        return all_actual_namefiles

    def start(self):
        if self.condition:
            self.logger.info("Чтение report.txt")
            with open(self.path_report, "r", encoding='utf-8') as f:
                report = f.readlines()
            f.close()
            self.logger.info("Чтение report.txt завершено")
            all_actual_name_files = self.__search_all_files(self.path_to_test)

            try:
                for counter in tqdm(range(0, len(all_actual_name_files), 3),desc="Progress",unit=" files", ncols=100):
                    # print("Выполнено - ", ((counter+1)/len(all_actual_name_files))*100, " %", end="\r")
                    filename_rtds = all_actual_name_files[counter]
                    filename_terminal_sub_a = all_actual_name_files[counter + 1]
                    filename_terminal_sub_b = all_actual_name_files[counter + 2]

                    rtds_comtrade = Parser_comtrade(path=filename_rtds)
                    terminal_sub_a_comtrade = Parser_comtrade(path=filename_terminal_sub_a)
                    terminal_sub_b_comtrade = Parser_comtrade(path=filename_terminal_sub_b)

                    rtds_comtrade.parse()
                    terminal_sub_a_comtrade.parse()
                    terminal_sub_b_comtrade.parse()

                    max_pos_brk1 = max(rtds_comtrade.matrix_digital[:, rtds_comtrade.name_digital.index("BRK1_D") + 1])
                    max_pos_brk4 = max(rtds_comtrade.matrix_digital[:, rtds_comtrade.name_digital.index("BRK4_D") + 1])
                    trips_sub_a, time_trips_sub_a = self.__get_info(self.list_signals_from_rtds_sub_a, rtds_comtrade)
                    trips_sub_b, time_trips_sub_b = self.__get_info(self.list_signals_from_rtds_sub_b, rtds_comtrade)
                    flt_in_test, start_flt = self.__get_info(self.list_flt, rtds_comtrade)

                    analyze_trips_sub_a = self.__analyze_oscill(trips_sub_a, time_trips_sub_a, flt_in_test, start_flt,
                                                                "ПСА", max_pos_brk1)
                    analyze_trips_sub_b = self.__analyze_oscill(trips_sub_b, time_trips_sub_b, flt_in_test, start_flt,
                                                                "ПСБ", max_pos_brk4)
                    analyze_strs_sub_a = self.__get_info(self.list_signals_from_terminal, terminal_sub_a_comtrade)[0]
                    analyze_strs_sub_b = self.__get_info(self.list_signals_from_terminal, terminal_sub_b_comtrade)[0]

                    result = analyze_trips_sub_a + analyze_trips_sub_b

                    for str_sub in analyze_strs_sub_a:
                        result = result + "5 / " + self.dictionary[str_sub] + "на ПСА" + "\n"
                    for str_sub in analyze_strs_sub_b:
                        result = result + "5 / " + self.dictionary[str_sub] + "на ПСБ" + "\n"

                    number_test = all_actual_name_files[counter].split("\\")[-1].split(" ")[6]
                    string_number_test_in_report = "1 / Опыт №" + str(number_test) + " \n"
                    try:
                        index_test_in_report = report.index(str(string_number_test_in_report))
                        index_separator = report.index(
                            "=======================================================================================================================\n",
                            index_test_in_report)
                        report.insert(index_separator, result)
                    except ValueError:
                        self.logger.debug(f"cannot get index test {number_test} in order to insert ")
                        continue
            except IndexError:
                self.logger.debug("no such file cfg or dat for a rtds comtrade " + all_actual_name_files[counter] + "\n")
            self.logger.info("Запись информации в новый репорт")
            with open(self.path_report, "w", encoding='utf-8') as f:
                for i in tqdm(range(len(report))):
                    f.write(report[i])
            self.logger.info("Запись информации в новый репорт завершена")
        else:
            self.logger.info("Writer info in report is blocked")