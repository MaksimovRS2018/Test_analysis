import configparser


class Configurator:
    def __init__(self, cfg):
        self.__cfg = cfg
        self.__configurator = configparser.ConfigParser()

    def __condition(self, x):
        if x == "ON":
            return True
        if x == "OFF":
            return False
        return None

    def get_mode(self, part_script):
        return self.__condition(self.__configurator["MODE_SCRIPT"][part_script])

    def read(self):
        self.__configurator.sections()
        self.__configurator.read(filenames=self.__cfg, encoding='utf-8')
        print(self.__configurator["SETTING_ANALYZE"]["dictionary"].split(",\n"))
