import pandas as pd


def table1(current_time, connection, table_logger):
    """
    :param current_time:
    :param connection:
    :return:none
    """
    sql = """select a,b,c from table1"""
    table_logger.info("table1(尝试读取)")
    try:
        df = pd.read_sql(sql, con=connection)
        table_logger.info("table1(读取成功)")
    except:
        table_logger.critical("table1(读取失败)")
    df.fillna(0, inplace=True)
    try:
        df.to_excel(current_time + "table1.xlsx", index=False)
        table_logger.info("table1(excel已生成)")
    except:
        table_logger.critical("table1(excel未生成)")

def table2(current_time, connection, table_logger):
    """
    :param current_time:
    :param connection:
    :return:none
    """
    sql = """select a,b,c from table1"""
    table_logger.info("table2(尝试读取)")
    try:
        df = pd.read_sql(sql, con=connection)
        table_logger.info("table2(读取成功)")
    except:
        table_logger.critical("table2(读取失败)")
    df.fillna(0, inplace=True)
    try:
        df.to_excel(current_time + "table2.xlsx", index=False)
        table_logger.info("table2(excel已生成)")
    except:
        table_logger.critical("table2(excel未生成)")

def table3(current_time, connection, table_logger):
    """
    :param current_time:
    :param connection:
    :return:none
    """
    sql = """select a,b,c from table1"""
    table_logger.info("table3(尝试读取)")
    try:
        df = pd.read_sql(sql, con=connection)
        table_logger.info("table3(读取成功)")
    except:
        table_logger.critical("table3(读取失败)")
    df.fillna(0, inplace=True)
    try:
        df.to_excel(current_time + "table1.xlsx", index=False)
        table_logger.info("table3(excel已生成)")
    except:
        table_logger.critical("table3(excel未生成)")
