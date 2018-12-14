import datetime
import sql_gen as sg
import logger
import cmprs
import mails
import cx_Oracle

def table1():
    sg.table1(current_time, connection, table_logger)
    table1_zip = cmprs.compress('table1', current_time, cmprs_logger)
    mails.send_email('table1', current_time, mail_logger, table1_zip)


def table2():
    sg.table2(current_time, connection, table_logger)
    table2_zip = cmprs.compress('table2', current_time, cmprs_logger)
    mails.send_email('table2', current_time, mail_logger, table2_zip)


def table3():
    sg.table3(current_time, connection, table_logger)
    table3_zip = cmprs.compress('table3', current_time, cmprs_logger)
    mails.send_email('table3', current_time, mail_logger, table3_zip)


def get_loggers():
    database_logger = logger.get_database_logger()
    table_logger = logger.get_table_logger()
    cmprs_logger = logger.get_cmprs_logger()
    mail_logger = logger.get_mail_logger()
    return database_logger, table_logger, cmprs_logger, mail_logger


def database_connection():
    try:
        connection = cx_Oracle.connect("user/password@192.168.0.1:1521/orcl", encoding="utf-8")
        database_logger.info("connecting to database successfully.")
    except:
        database_logger.critical("connecting to database failed.")
    return connection


now = datetime.datetime.now()
hour = now.hour
minute = now.minute
weekday = datetime.datetime.isoweekday(now)
current_time = str(now.year) + str(now.month) + str(now.day) + "-" + str(now.hour) + "-" + str(now.minute)
# --------------------------------------------------------
# --------------------------------------------------------
database_logger, table_logger, cmprs_logger, mail_logger = get_loggers()
connection = database_connection()
if weekday == 5 and hour == 15:
    try:
        table1()
    except:
        pass
if weekday == 5 and hour == 15:
    try:
        table2()
    except:
        pass
if hour == 15:
    try:
        table3()
    except:
        pass
