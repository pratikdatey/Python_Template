## Logging

import logging
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}"
logs_path = os.path.join(os.getcwd(), 'logs',LOG_FILE)
os.makedirs(logs_path,exist_ok=True)


LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] -%(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)




## Exception
import sys
import logging

def error_mesasge_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_mesasge="Error occurred in python script name[{0}] line number[{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))

    return error_mesasge


class CustomException(Exception):
    def __init__(self,error_mesasge,error_detail:sys):
        super().__init__(error_mesasge)
        self.error_mesasge=error_mesasge_detail(error_mesasge,error_detail=error_detail)



    def __str__(self):
        return self.error_mesasge
    
