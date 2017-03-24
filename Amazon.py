'''
Created on 17-Mar-2017

@author: prince.mahi
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from lib2to3.tests.support import driver
from selenium.webdriver import ActionChains



if __name__ == '__main__':
    
    driver = webdriver.Firefox()
    driver.get("https://www.irctc.in")
    driver.find_element_by_xpath("")
    
   