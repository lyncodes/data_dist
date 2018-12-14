import os
import mails


def compress(choice, current_time, cmprs_logger):
    choice == ' '
    try:
        paras = mails.read_email_para()
        password = paras[(paras['active'] == 'Y') & (paras['file_name'] == 'choice')]['cmprpwd'].values[0]
        compress_command = "7z a -p" + password + " " + current_time + choice + ".zip " + current_time + choice + ".xlsx"
        cmprs_logger.info(choice + "(压缩成功)")
        zipname = current_time + choice + ".zip "
        os.system(compress_command)
        return zipname
    except:
        cmprs_logger.critical(choice + "(压缩失败)")
    # multiple files compress command:
    # compress_command = "7z a -p" + password + " " + current_time + choice+".zip " + \
    #             sheet_name_1 + ".xlsx " + \
    #             sheet_name_2 + ".xlsx " + \
    #             sheet_name_3 + ".txt " + \
    #             sheet_name_4 + ".txt"
