#  coding=utf-8
from config import globalparam
class Screen(object):
    """截图功能装饰器"""
    def __init__(self, driver):
        self.driver = driver
    def __call__(self, f):
        def inner(*args):
            try:
                return f(*args)
            except:
                import time
                nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
                file_name = '%s.jpg' % nowTime
                file_path = globalparam.exception_path + "\\" + file_name
                self.driver.get_screenshot_as_file(file_path)
                raise
        return inner
