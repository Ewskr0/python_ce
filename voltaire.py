from selenium import webdriver
from selenium.webdriver.common.keys import Keys

usr_name = input('User name :')
usr_pss = input('User password :')
webpage = "https://www.projet-voltaire.fr/"

driver = webdriver.Firefox()
driver.get(webpage)

usr_name_box = driver.find_element_by_id("login-username")
usr_name_box.send_keys(usr_name)

usr_pss_box = driver.find_element_by_id("login-pwd")
usr_pss_box.send_keys(usr_ss)

