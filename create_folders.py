
config = "config.txt"
import os

with open(config, "r", encoding='utf-8') as conf:
    a = conf.readlines()
    for i in range(len(a)):
        try:
            number_test = a[i].split("\n")[0]
            path = "D:\\rtds_test\\tests\\"
            new_folder =""
            for k in range(len(number_test.split(".")) - 1):
                new_folder = new_folder + number_test.split(".")[k] + "."
                path = path + new_folder + "/"
            path = path + "/" +  number_test
            os.makedirs(path)
        except FileExistsError:
            continue
    conf.close()
