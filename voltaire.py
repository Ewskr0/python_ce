import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

usr_name = 'ewann.villa@epita.fr' #input('User name :')
usr_pss =  '123.Banane' #getpass.getpass('User password :')
webpage = "https://www.projet-voltaire.fr/"

driver = webdriver.Firefox()
driver.get(webpage)


buttonlog = driver.find_element_by_id("authenticateOption")
buttonlog.click()

usr_name_box = driver.find_element_by_id("login-username")
usr_name_box.clear()
usr_name_box.send_keys(usr_name)

usr_pss_box = driver.find_element_by_id("login-pwd")
usr_pss_box.clear()
usr_pss_box.send_keys(usr_pss)

login_box = driver.find_element_by_name("input_validate")
login_box.click()
