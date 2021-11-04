from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

flag = 0

path = "C:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://lms.iiitkottayam.ac.in/my/")

def login(user, pwd):
    global driver
    user_name = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")

    user_name.send_keys(user)
    password.send_keys(pwd)
    password.send_keys(Keys.ENTER)
    
    




def notify(a,b,c):
    

    global driver    
    driver.get(a)

    find_link = driver.find_element_by_xpath(b)

    find_link.click()

    if c == "zoom":
        join = driver.find_element_by_xpath('//*[@id="region-main"]/div[1]/div[1]/form')
        join.click()
        
#driver.quit()
        

        
        
    
