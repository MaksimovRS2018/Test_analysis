# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print('START')
import logging
from datetime import datetime
from datetime import timedelta
from CustomFormatter import CustomFormatter
from create_folders import create_folders_for_tests
from ComparatorFiles import ComparatorFiles
from Writter_info_in_report import Writter_info_in_report
# logging.basicConfig(level="DEBUG", filename="mylog.log")

actual_time = datetime.utcnow() + timedelta(hours=3)
data_now = str(actual_time).split(" ")[0]
time_now = str(actual_time).split(" ")[1]
name_log_file = data_now + ".log"
handler_file = logging.FileHandler(name_log_file,"w",encoding = "UTF-8")
handler_file.setLevel(logging.DEBUG)
handler_file.setFormatter(CustomFormatter())
handler_console = logging.StreamHandler()
handler_console.setLevel(logging.DEBUG)
handler_console.setFormatter(CustomFormatter())
handlers = [handler_file, handler_console]
logger = logging.getLogger("Logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler_file)
logger.addHandler(handler_console)

path_to_tests = f"D:\\rtds_test\\tests_{data_now}\\"
path_to_RTDS = "D:\\YandexDisk\\Test2\\KSZ"
path_to_terminal = "D:\\YandexDisk\\Test\\KSZ 500\\Terminals\\"



logger.info("info")
config_folder = "config_folder.cfg"

logger.info("START PROCESS")
logger.info("CREATION FOLDERS START")
create_folders_for_tests(config_folder, path_to_tests)
logger.info("CREATION FOLDERS FINISH")
comparator = ComparatorFiles(logger=logger,
                             path_to_RTDS=path_to_RTDS,
                             path_to_terminal=path_to_terminal,
                             path_to_test_folders=path_to_tests)
comparator.start()
