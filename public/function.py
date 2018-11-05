# coding=utf-8
from public.base import Page
from config import globalparam

def insert_img(driver, file_name):
    """Screenshot function"""
    file_path = globalparam.img_path + '\\' + file_name
    Page(driver).take_screenshot(file_path)

if __name__ =="__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    insert_img(driver, file_name='bidu_home_0.png')
    driver.quit()
