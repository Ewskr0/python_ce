import getpass
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def check_find_element_by_id(el):
    try:
        driver.find_element_by_id(el)
    except NoSuchElementException:
        return False
    return True

def check_find_element_by_class_name(el):
    try:
        driver.find_element_by_class_name(el)
    except NoSuchElementException:
        return False
    return True
    
def popup():
		time.sleep(1)
		if check_find_element_by_class_name("understoodButton"):
			time.sleep(2)
			under_box = driver.find_element_by_class_name("understoodButton")
			under_box.click()

			while not check_find_element_by_class_name("buttonOk"):
				time.sleep(0.2)
			ok_box = driver.find_elements_by_class_name("buttonOk")
			for e in ok_box:
				e.click();
				time.sleep(0.2)
			exit_box = driver.find_element_by_class_name("exitButton")
			exit_box.click()
			time.sleep(1)



# START 

deltaT = 10

data = open('data.txt', 'r+')
lines = data.readline()
for e in lines:
	e.split("|")

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
	iscorrect = False
	popup()
	while not check_find_element_by_class_name("sentence"):
		time.sleep(0.2)
	sentence = driver.find_element_by_class_name("sentence").text

	for e in lines:
		if e[0] == sentence:
			present = True

	popup()
	fault_box = driver.find_element_by_id("btn_pas_de_faute")
	fault_box.click()

	x = 0
	while x < deltaT and not check_find_element_by_class_name("answerWord"):
		time.sleep(0.5)
		x += 1
	if x == 10:
		iscorrect = True
	
	if not present and not iscorrect:
		answer = driver.find_element_by_class_name("answerWord").text

	if not present:
		data.writelines(sentence+"|"+answer+"\n")
		print("line added : "+sentence+"|"+answer)

	popup()
	while not check_find_element_by_id("btn_question_suivante"):
		time.sleep(0.2)
	next_box = driver.find_element_by_id("btn_question_suivante")
	next_box.click()







import getpass
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def check_find_element_by_id(el):
    try:
        driver.find_element_by_id(el)
    except NoSuchElementException:
        return False
    return True

def check_find_element_by_class_name(el):
    try:
        driver.find_element_by_class_name(el)
    except NoSuchElementException:
        return False
    return True
    
def popup():
		time.sleep(1)
		if check_find_element_by_class_name("understoodButton"):
			time.sleep(2)
			under_box = driver.find_element_by_class_name("understoodButton")
			under_box.click()

			while not check_find_element_by_class_name("buttonOk"):
				time.sleep(0.2)
			ok_box = driver.find_elements_by_class_name("buttonOk")
			for e in ok_box:
				e.click();
				time.sleep(0.2)
			exit_box = driver.find_element_by_class_name("exitButton")
			exit_box.click()
			time.sleep(1)



# START 

deltaT = 10

data = open('data.txt', 'r+')
lines = data.readline()
for e in lines:
	e.split("|")

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
	iscorrect = False
	popup()
	while not check_find_element_by_class_name("sentence"):
		time.sleep(0.2)
	sentence = driver.find_element_by_class_name("sentence").text

	for e in lines:
		if e[0] == sentence:
			present = True

	popup()
	fault_box = driver.find_element_by_id("btn_pas_de_faute")
	fault_box.click()

	x = 0
	while x < deltaT and not check_find_element_by_class_name("answerWord"):
		time.sleep(0.5)
		x += 1
	if x == 10:
		iscorrect = True
	
	if not present and not iscorrect:
		answer = driver.find_element_by_class_name("answerWord").text

	if not present:
		data.writelines(sentence+"|"+answer+"\n")
		print("line added : "+sentence+"|"+answer)

	popup()
	while not check_find_element_by_id("btn_question_suivante"):
		time.sleep(0.2)
	next_box = driver.find_element_by_id("btn_question_suivante")
	next_box.click()







