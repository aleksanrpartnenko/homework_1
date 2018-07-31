from selenium import webdriver
from selenium.webdriver.common.keys import Keys
i=0
User_LIST = ["Jonas M", "Jurgis X", "Vaidas L"]
Plate_LIST =["acv345", "klm059", "odp543"]
driver = webdriver.Firefox()
driver.get("http://127.0.0.1:8000/angular")#put here the adress of your page
while i < len(User_LIST):
    user = driver.find_element_by_id("NAMEID")
    plate = driver.find_element_by_id("PLATEID")

    user.send_keys(User_LIST[i])
    plate.send_keys(Plate_LIST[i])
    driver.find_element_by_name("submit").click()
    i+=1

#elem = driver.find_elements_by_xpath("//*[@id=\"demoApp\"]/button")#put here the content you have put in Notepad, ie the XPath
#print(elem .get_attribute("class"))
driver.close()