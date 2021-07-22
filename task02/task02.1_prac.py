import selenium
from selenium import webdriver

driver = webdriver.Chrome('C:\Download\driver\chromedriver.exe')
driver.implicitly_wait(3)


def login(user_id, user_pw):
    driver.get('https://leetcode.com/accounts/google/login/?next=%2F')
    driver.find_element_by_name('identifier').send_keys(user_id)
    driver.find_element_by_class_name('VfPpkd-vQzf8d').click()
    driver.find_element_by_name('password').send_keys(user_pw)
    driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()

if __name__ == "__main__":
    login('student13@bible.ac.kr', '********')


