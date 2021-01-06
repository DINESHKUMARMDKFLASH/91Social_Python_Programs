import logging
import logging.handlers as handlers
from datetime import datetime

backupCount = int(input("How many backup log files do you want ? ( 0 - 99 ) : "))
logger = logging.getLogger('my_log')
logger.setLevel(logging.INFO)
logHandler = handlers.RotatingFileHandler('log_backup_file.log', maxBytes=2 * 1024 * 1024, backupCount=backupCount)
logger.addHandler(logHandler)

while True:
    logger.info(datetime.now().strftime("%m-%d %H:%M:%S.%f") + "\n")
