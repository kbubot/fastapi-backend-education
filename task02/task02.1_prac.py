import selenium
from selenium import webdriver

driver = webdriver.Chrome('C:\Download\driver\chromedriver.exe')
driver.implicitly_wait(3)


def login(user_id, user_pw):
    driver.get('https://leetcode.com/accounts/login/')
    driver.find_element_by_name('login').send_keys(user_id)
    driver.find_element_by_name('password').send_keys(user_pw)
    driver.find_element_by_id('signin_btn').click()


if __name__ == "__main__":
    login('22th_king', '*************')


