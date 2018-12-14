import logging
import datetime
# add database logger
def get_database_logger():
    now = datetime.datetime.now()
    current_time = str(now.year)+str(now.month)+str(now.day)+"-"+str(now.hour)+"-"+str(now.minute)
    #---------------------------------------------------------
    database_logger = logging.getLogger("sql_log")
    database_logger.setLevel(level = logging.INFO)

    database_handler = logging.FileHandler(current_time+".log")
    database_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
    database_handler.setFormatter(formatter)

    database_logger.addHandler(database_handler)
    return database_logger

# add table generation logger
def get_table_logger():
    now = datetime.datetime.now()
    current_time = str(now.year)+str(now.month)+str(now.day)+"-"+str(now.hour)+"-"+str(now.minute)
    #---------------------------------------------------------
    table_logger = logging.getLogger("table_log")
    table_logger.setLevel(level = logging.INFO)

    table_handler = logging.FileHandler(current_time+".log")
    table_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
    table_handler.setFormatter(formatter)

    table_logger.addHandler(table_handler)
    return table_logger
# add compress logger
def get_cmprs_logger():
    now = datetime.datetime.now()
    current_time = str(now.year)+str(now.month)+str(now.day)+"-"+str(now.hour)+"-"+str(now.minute)
    #---------------------------------------------------------
    cmprs_logger = logging.getLogger("compress_log")
    cmprs_logger.setLevel(level = logging.INFO)

    cmprs_handler = logging.FileHandler(current_time+".log")
    cmprs_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
    cmprs_handler.setFormatter(formatter)

    cmprs_logger.addHandler(cmprs_handler)
    return cmprs_logger

def get_mail_logger():
    now = datetime.datetime.now()
    current_time = str(now.year)+str(now.month)+str(now.day)+"-"+str(now.hour)+"-"+str(now.minute)
    #---------------------------------------------------------
    mail_logger = logging.getLogger("mail_log")
    mail_logger.setLevel(level = logging.INFO)

    mail_handler = logging.FileHandler(current_time+".log")
    mail_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
    mail_handler.setFormatter(formatter)

    mail_logger.addHandler(mail_handler)
    return mail_logger
