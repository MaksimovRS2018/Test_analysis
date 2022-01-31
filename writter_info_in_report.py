from Parser_comtrade import Parser_comtrade
import numpy as np

list_signals_from_rtds_sub_a = ["TRIP_DZ_1_st_SUB_A", "TRIP_DZ0_1_st_SUB_A", "TRIP_DZ_2_st_SUB_A", "TRIP_DZ_3_st_SUB_A",
                                "TRIP_TNZNP_1_st_SUB_A", "TRIP_TNZNP_2_st_SUB_A", "TRIP_TNZNP_3_st_SUB_A",
                                "TRIP_phA_SUB_A", "TRIP_phB_SUB_A", "TRIP_phC_SUB_A", "OTF_SUB_A", "SEND_VCH2_SUB_A",
                                "TRIP_BNN_A"]
list_signals_from_rtds_sub_b = ["TRIP_DZ_1_st_SUB_B", "TRIP_DZ0_1_st_SUB_B", "TRIP_DZ0_1_st_SUB_B",
                                "TRIP_DZ_3_st_SUB_B",
                                "TRIP_TNZNP_1_st_SUB_B", "TRIP_TNZNP_2_st_SUB_B", "TRIP_TNZNP_3_st_SUB_B",
                                "TRIP_phA_SUB_B", "TRIP_phB_SUB_B", "TRIP_phC_SUB_B", "OTF_SUB_B", "SEND_VCH2_SUB_B"]
list_signals_from_terminal = [
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

list_flt = ["FLT1", "FLT2", "FLT3", "FLT4", "FLT5", "FLT6", "FLT7", "FLT8", "FLT9", "FLT1.1", "FLT1.2", "FLT1.3"]
list_flt_int = ["FLT1", "FLT5", "FLT1.1", "FLT1.2", "FLT1.3"]
list_flt_ext = ["FLT2", "FLT3", "FLT4", "FLT6", "FLT7", "FLT8", "FLT9"]

dictionary = {
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


def get_info(list_name_signals, parser_comtrade):
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


def analyze_oscill(list_trip_sub, list_time_trip_sub, flts_in_test, times_start_flt, name_sub, brk):
    text = ""
    if len(flts_in_test) >= 1:  # если в опыте есть КЗ
        if len(list_trip_sub) == 0:  # если отсутствуют срабатывания при наличии кз
            text = text + "Отсутствие срабатывания защиты на " + name_sub + '\n'
            if flts_in_test[0] in list_flt_int:  # если кз внутренеее и нет срабатывания
                if brk == 1:
                    text = text + "Отказ срабатывания защиты на " + name_sub + '\n'
        else:  # если есть срабатывания при наличии кз
            if flts_in_test[0] in list_flt_ext:  # если кз внешнее
                text = text + "Излишнее срабатывания защиты на " + name_sub + '\n'
            for trip_prot_one_sub in range(len(list_trip_sub)):
                text = text + dictionary[list_trip_sub[trip_prot_one_sub]] + " : " + \
                       str(np.round(list_time_trip_sub[trip_prot_one_sub] - min(times_start_flt), decimals=5)) + ' c \n'
    else:  # если в опыте нет КЗ
        if len(list_trip_sub) == 1:  # если отсутствуют срабатывания при наличии кз
            text = text + "Ложное срабатывание защиты на " + name_sub + '\n'

    return text


filename_rtds = "D:\\rtds_test\\tests\\3\\3.1\\3.1.1\\Number start = 1 Test = 3.1.1.1.1 Time = 01_26_2022 12_14_11.369 RTDS "
filename_terminal_sub_a =  "D:\\rtds_test\\tests\\3\\3.1\\3.1.1\\Number start = 1 Test = 3.1.1.1.1 Time = 01_26_2022 12_14_11.369 Terminal ПСА 002D0010"
filename_terminal_sub_b =  "D:\\rtds_test\\tests\\3\\3.1\\3.1.1\\Number start = 1 Test = 3.1.1.1.1 Time = 01_26_2022 12_14_11.369 Terminal ПСБ 001D0010"

filenames = [filename_rtds, filename_terminal_sub_a, filename_terminal_sub_b]


rtds_comtrade = Parser_comtrade(path=filename_rtds)
terminal_sub_a_comtrade = Parser_comtrade(path=filename_terminal_sub_a)
terminal_sub_b_comtrade = Parser_comtrade(path=filename_terminal_sub_b)

rtds_comtrade.parse()
terminal_sub_a_comtrade.parse()
terminal_sub_b_comtrade.parse()

max_pos_brk1 = max(rtds_comtrade.matrix_digital[:, rtds_comtrade.name_digital.index("BRK1_D") + 1])
max_pos_brk4 = max(rtds_comtrade.matrix_digital[:, rtds_comtrade.name_digital.index("BRK4_D") + 1])
trips_sub_a, time_trips_sub_a = get_info(list_signals_from_rtds_sub_a, rtds_comtrade)
trips_sub_b, time_trips_sub_b = get_info(list_signals_from_rtds_sub_b, rtds_comtrade)
flt_in_test, start_flt = get_info(list_flt, rtds_comtrade)

text_sub_a = analyze_oscill(trips_sub_a, time_trips_sub_a, flt_in_test, start_flt, "ПСА", max_pos_brk1)
text_sub_b = analyze_oscill(trips_sub_b, time_trips_sub_b, flt_in_test, start_flt, "ПСБ", max_pos_brk4)
strs_sub_a = get_info(list_signals_from_terminal,terminal_sub_a_comtrade)[0]
strs_sub_b = get_info(list_signals_from_terminal,terminal_sub_b_comtrade)[0]

all_text = text_sub_a + text_sub_b
for str_sub in strs_sub_a:
    all_text = all_text + dictionary[str_sub] + "\n"
for str_sub in strs_sub_b:
    all_text = all_text + dictionary[str_sub] + "\n"