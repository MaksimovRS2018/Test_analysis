import numpy
import matplotlib.pyplot as plt


class Parser_comtrade():
    def __init__(self, path="2", flag="224 Пуск осциллогр.", time_d=20000 / 24, A=True, D=True, dscr = 15):
        self.__path_cfg = path + ".cfg"
        self.__path_dat = path + ".dat"
        self.__data_A = {}
        self.__data_B = {}
        self.name_analog = []
        self.name_digital = []
        self.data_analog = {}
        self.__flag = flag
        self.time_d = time_d
        self.end_time = 600000
        self.index_end_time = -1
        self.__numbers_analog = 0
        self.__numbers_digital = 0
        self.numbers_signal = 0
        self.matrix_analog = numpy.zeros((1, 1))
        self.matrix_digital = numpy.zeros((1, 1))
        self.index_time = -1
        self.data_cfg = []
        self.data_dat = []
        self.__A = A
        self.__D = D
        self.new_time_d = 0
        self.dscr = dscr


    def parse(self):
        self.__parse_cfg()
        self.__parse_dat()


    def __parse_cfg(self):
        with open(self.__path_cfg, 'r') as fp:
            self.data_cfg = fp.readlines()
            self.__numbers_analog = int(self.data_cfg[1].split(",")[1].split("A")[0])
            self.__numbers_digital = int(self.data_cfg[1].split(",")[2].split("D")[0])
            for number_analog in range(self.__numbers_analog):
                self.name_analog.append(self.data_cfg[2 + number_analog].split(",")[1])
                self.__data_A[self.data_cfg[2 + number_analog].split(",")[1]] = float(
                    self.data_cfg[2 + number_analog].split(",")[5])
                self.__data_B[self.data_cfg[2 + number_analog].split(",")[1]] = float(
                    self.data_cfg[2 + number_analog].split(",")[6])
            for number_digital in range(self.__numbers_analog, self.__numbers_analog + self.__numbers_digital):
                self.name_digital.append(self.data_cfg[2 + number_digital].split(",")[1])
            self.numbers_signal = self.__numbers_analog + self.__numbers_digital
        fp.close()

    def __parse_dat(self):
        with open(self.__path_dat, 'r') as fp:

            self.data_dat = fp.readlines()
            self.time_d = int(self.data_dat[1].split(",")[1])
            self.end_time = int(self.data_dat[len(self.data_dat) - 1].split(",")[1])
            self.index_end_time = int(self.data_dat[len(self.data_dat) - 1].split(",")[0])
            size_matrix = int(len(self.data_dat)/self.dscr)
            self.matrix_digital = numpy.zeros((size_matrix, self.__numbers_digital + 1))
            self.new_time_d = self.time_d * self.dscr
            self.times = list(range(0, self.matrix_digital.shape[0]*self.new_time_d, self.new_time_d))
            for t in range(len(self.times)):
                index = int(self.times[t]/self.time_d)
                self.matrix_digital[t, 0] = int(self.data_dat[index].split(",")[1])
                for number_digital in range(self.__numbers_digital):
                    self.matrix_digital[t, number_digital + 1] = int(
                        self.data_dat[index].split(",")[2 + self.__numbers_analog + number_digital])

        fp.close()



