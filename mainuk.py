import sys
print (sys.argv)
import time
import names
from selenium import webdriver

print("KRISPY KREME ACCOUNT MAKER MADE BY Mr.Bean#0101")
print("Please enter your Email: ")
email = input("")
password = "DjwkhadSDAdyWdhSJ@!321"
print("password = DjwkhadSDAdyWdhSJ@!321")



def order():

    driver.find_element_by_xpath('//*[@id="p_lt_WebPartZone3_Footer_SimpleCookieLawConsent_btnAllowAll"]').click()
    driver.find_element_by_xpath('//*[@id="p_lt_WebPartZone2_Content_pageplaceholder_p_lt_WebPartZone3_MainContent_Register_txtFirstName"]').send_keys(names.get_first_name())
    driver.find_element_by_xpath('//*[@id="p_lt_WebPartZone2_Content_pageplaceholder_p_lt_WebPartZone3_MainContent_Register_txtLastName"]').send_keys(names.get_last_name())
    driver.find_element_by_xpath('//*[@id="p_lt_WebPartZone2_Content_pageplaceholder_p_lt_WebPartZone3_MainContent_Register_txtEmail"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="p_lt_WebPartZone2_Content_pageplaceholder_p_lt_WebPartZone3_MainContent_Register_txtPassword"]').send_keys("DjwkhadSDAdyWdhSJ@!321")
    driver.find_element_by_xpath('//*[@id="p_lt_WebPartZone2_Content_pageplaceholder_p_lt_WebPartZone3_MainContent_Register_txtConfirmPassword"]').send_keys("DjwkhadSDAdyWdhSJ@!321")
    driver.find_element_by_xpath('//*[@id="p_lt_WebPartZone2_Content_pageplaceholder_p_lt_WebPartZone3_MainContent_Register_btnSubmit"]').click()

    print("Account Has Been Created!")
    print("Username/email = "+email)
    print("Password = "+password)
    print("MADE BY Mr.Bean#0101")

if __name__ == '__main__':
    #load chrome
   driver = webdriver.Chrome('./chromedriver')

   driver.get("https://www.krispykreme.co.uk/register")
   order()
