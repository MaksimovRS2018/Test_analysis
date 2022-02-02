# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print('START')
import logging
from datetime import datetime
from datetime import timedelta
from classes.optional.CustomFormatter import CustomFormatter
from functions.create_folders import create_folders_for_tests
from classes.functional.CopyWriterComparatorFiles import CopyWriterComparatorFiles
from classes.functional.Writer_info_in_report import Writer_info_in_report
from classes.optional.Configurator import Configurator

actual_time = datetime.utcnow() + timedelta(hours=3)
data_now = str(actual_time).split(" ")[0]
time_now = str(actual_time).split(" ")[1]
name_log_file = f"logs\\{data_now}.log"

handler_file = logging.FileHandler(name_log_file, "w", encoding="UTF-8")
handler_file.setLevel(logging.DEBUG)
handler_file.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"))

handler_console = logging.StreamHandler()
handler_console.setLevel(logging.DEBUG)
handler_console.setFormatter(CustomFormatter())

logger = logging.getLogger("Logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler_file)
logger.addHandler(handler_console)

path_to_test_folders = f"D:\\rtds_test\\tests_{data_now}\\"
path_to_RTDS = "D:\\YandexDisk\\Test2\\KSZ"
path_to_terminal = "D:\\YandexDisk\\Test\\KSZ 500\\Terminals\\"
config_folder = "configs\\config_folder.cfg"
config_script = "configs\\script.cfg"


configurator = Configurator(config_script)
configurator.read()

logger.info("START PROCESS")

if configurator.get_mode("create_folders"):
    logger.info("CREATION FOLDERS START")
    create_folders_for_tests(config_folder, path_to_test_folders)
    logger.info("CREATION FOLDERS FINISH")

comparator = CopyWriterComparatorFiles(logger=logger,
                                       path_to_RTDS=path_to_RTDS,
                                       path_to_terminal=path_to_terminal,
                                       path_to_test_folders=path_to_test_folders,
                                       condition = configurator.get_mode("copywriter_comparator")
                                       )
comparator.start()
comparator.copy_report()
writer = Writer_info_in_report(logger=logger,
                               path_to_tests=path_to_test_folders,
                               condition=configurator.get_mode("writer_report")
                               )
writer.start()

logger.info("STOP PROCESS")