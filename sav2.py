import getpass
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def check_find_element_by_id(el):
    try:
        test = driver.find_element_by_id(el)
        
    except NoSuchElementException:
        return False
    return test.is_displayed()

def check_find_element_by_class_name(el):
    try:
        test = driver.find_element_by_class_name(el)
    except NoSuchElementException:
        return False
    return test.is_displayed()
    
def is_disp(e):
	while not e.is_displayed():
		time.sleep(0.2)

def popup():
		time.sleep(1)

		if check_find_element_by_class_name("understoodButton"):

			under_box = driver.find_element_by_class_name("understoodButton")
			is_disp(under_box)
			under_box.click()
			while not check_find_element_by_class_name("buttonOk"):
				time.sleep(0.1)
			ok_box = driver.find_elements_by_class_name("buttonOk")
			for e in ok_box:
				is_disp(e)
				e.click();
				time.sleep(0.1)
			exit_box = driver.find_element_by_class_name("exitButton")
			is_disp(exit_box)
			exit_box.click()
			time.sleep(0.5)

def buttons_next():
		if check_find_element_by_id("btn_question_suivante"):
			next_box = driver.find_element_by_id("btn_question_suivante")
			next_box.click()
			time.sleep(0.5)
			return True
		return False

def buttons_falt():
		if check_find_element_by_id("btn_pas_de_faute"):
			fault_box = driver.find_element_by_id("btn_pas_de_faute")
			fault_box.click()
			time.sleep(0.2)
			return True
		return False
		
# START 


data = open('data.txt', 'r+')

usr_name = 'ewann.pelle@epita.fr' #input('User name :')
usr_pss =  '123.Banane' #getpass.getpass('User password :')
webpage = "https://www.projet-voltaire.fr/"

driver = webdriver.Firefox()
driver.get(webpage)

while not check_find_element_by_id("authenticateOption"):
	time.sleep(2)

buttonlog = driver.find_element_by_id("authenticateOption")
buttonlog.click()


while not check_find_element_by_id("login-username"):
	time.sleep(2)

usr_name_box = driver.find_element_by_id("login-username")
usr_name_box.clear()
usr_name_box.send_keys(usr_name)

usr_pss_box = driver.find_element_by_id("login-pwd")
usr_pss_box.clear()
usr_pss_box.send_keys(usr_pss)

time.sleep(0.5)

login_box = driver.find_element_by_name("input_validate")
login_box.click()



while not check_find_element_by_id("activityCellDiv_1"):
	time.sleep(0.5)

print(driver.current_url)
activity_box = driver.find_element_by_id("activityCellDiv_1")
activity_box.click()


while  True:
	present = False
	answer =""
	popup()
	while not check_find_element_by_class_name("sentence"):
		time.sleep(0.2)
	sentence = driver.find_element_by_class_name("sentence").text

	popup()
	while not buttons_falt():
		time.sleep(0.2)
	popup()
	while not check_find_element_by_class_name("gwt-InlineHTML"):
		buttons_falt()
		time.sleep(0.2)
	
	if check_find_element_by_class_name("answerWord"):
		answer = driver.find_element_by_class_name("answerWord").text

	data.writelines(sentence+"|"+answer+"\n")
	print("line added : "+sentence+"|"+answer)

	popup()
	while not buttons_next():
		time.sleep(0.2)
	buttons_next()


	













