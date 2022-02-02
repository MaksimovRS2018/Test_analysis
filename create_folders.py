import os


def create_folders_for_tests(config="config_folder.cfg", path_to_tests="D:\\rtds_test\\tests_01.02.2022\\"):
    with open(config, "r", encoding='utf-8') as conf:
        a = conf.readlines()
        for i in range(len(a)):
            try:
                number_test = a[i].split("\n")[0]
                path = path_to_tests
                new_folder = ""
                for k in range(len(number_test.split(".")) - 1):
                    new_folder = new_folder + number_test.split(".")[k] + "."
                    path = path + new_folder + "/"
                path = path + "/" + number_test
                os.makedirs(path)
            except FileExistsError:
                continue
        conf.close()
