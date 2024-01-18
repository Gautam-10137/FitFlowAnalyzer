# sys represents system , it will give details about python interpreter
import sys
 
from src.logger import logging
def error_detail_setter(error_message,error_detail:sys):
    # exception.info() return 3 things
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error="Error occured in python script name[{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error_message)
    )
    return error



# error detail object contains info about error occured in which file, lineno . 
# we have to extract these details and then return error message containing info about 
# what is error (message), occured in which file, line_no 
class CustomException(Exception):  # inheriting Exception class
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_detail_setter(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message
    
if __name__=="__main__":
    a=10
    try:
        print(a/0)
    except Exception as e:
        error_message=CustomException(e,sys)
        logging.info(error_message)




