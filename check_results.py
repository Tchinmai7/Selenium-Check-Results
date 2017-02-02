#Usage - Create an input file with list of reg_no and dob seperated by commas, one per line.
#Example input.txt follows
#2012124124124,04-07-1998
#3241431421421,07-04-1992
#and so on. To run the script, use python3 check_results.py input.txt
#The result will be saved as a screenshot with the reg_no as the file name.
#Needs selenium and python3 installed.
##Captcha has to be manually entered. Wait for the script to fill in the regno and date, and then enter captcha.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import base64
import sys
## Selenium web drivers
driver = None

def wait(web_opening_time=10):
	time.sleep(web_opening_time)

## load web driver for selenium : chrome
def web_driver_load():
	global driver
	driver = webdriver.Chrome()
## quit web driver for selenium
def web_driver_quit():
	driver.quit()

def site_open():
	driver.get('http://coe1.annauniv.edu');
	wait(5)

#email_ids= ['','fake@fake.com','tarun@herotalkies.com'];
#passwords=['','fake','123thisisit'];

regnos= [];
dobs=[];
def login(reg_no,dob):
	regnoElement=driver.find_element_by_xpath("//*[@id=\"register_no\"]")
	dobElement=driver.find_element_by_xpath("//*[@id=\"dob\"]")
	captchaElement=driver.find_element_by_xpath("//*[@id=\"login_stu\"]/div/div[3]/label/img")
	prefix="data:image/png;base64,"
	regnoElement.clear()
	regnoElement.send_keys(reg_no)
	dobElement.clear()
	dobElement.send_keys(dob)
	wait(10)
	dobElement.submit()

def test_logout():
	print ("testing Logout")
	try:
		logout = driver.find_element_by_xpath("//*[@id=\"content\"]/div[1]/a")
		logout.click()
	except:
		wait(3)
		pass

def is_page_loaded():
	try:
	        regnoElement=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"register_no\"]")))
	except:
		pass
		return false
	return true

def check_result(reg_no):
	element = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"tab4\"]")))
	element.click()
	resultsTab = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"resulttable\"]/tbody/tr[1]/td/table/tbody/tr[1]/th[2]")))
	driver.save_screenshot(reg_no+".png")

def parse_file(filename):
	with open(filename) as f:
		for line in f:
			entry=line.strip().split(',')
			regnos.append(entry[0])
			dobs.append(entry[1])
			print(entry)
### Main Method
if __name__ == "__main__":
	parse_file(sys.argv[1])
	web_driver_load()
	site_open()

	for i in range(len(regnos)):
		while(not is_page_loaded):
			try:
				site_open()
			except:
				wait(10)
				pass
				site_open()
		login(regnos[i],dobs[i])
		wait(3)
		check_result(regnos[i])
		test_logout()
	web_driver_quit()