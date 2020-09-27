#ivri korem 2020
"""
Travler is a bot i made whis selenium python for practice and fun,
it makes the proscces of getting flight tickets much cooler.
"""
#import
from SideFiles.Utilities.SelHelper import SelHelper
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import os
import random
import time

#Welcoming
print("""
████████╗██████╗░░█████╗░██╗░░░██╗███████╗██╗░░░░░███████╗██████╗░
╚══██╔══╝██╔══██╗██╔══██╗██║░░░██║██╔════╝██║░░░░░██╔════╝██╔══██╗
░░░██║░░░██████╔╝███████║╚██╗░██╔╝█████╗░░██║░░░░░█████╗░░██████╔╝
░░░██║░░░██╔══██╗██╔══██║░╚████╔╝░██╔══╝░░██║░░░░░██╔══╝░░██╔══██╗
░░░██║░░░██║░░██║██║░░██║░░╚██╔╝░░███████╗███████╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝""")

#Getting Input from the user
WebBrowser = input("What browser do you use? ").lower()
tripType = input("What type of trip you want? ")
departCity = input("Where do you want to depart from? ")
targetCity = input("Where do you want to fly to? ")
departMonth = input("in What month do you want to depart? ")
departDay = input("in What day in the month do you want to depart? ")

if tripType == "Roundtrip":
    #exclusive inputs for this type
    returnMonth = input("in What month do you want to return? ")
    returnDay = input("in What day in the month do you want to return? ")

#Init
if WebBrowser == "chrome":
    DriverLocation = "ThePath to the chromedriver in the repo"
    os.environ["webdriver.chrome.driver"] = DriverLocation
    driver = webdriver.Chrome(executable_path=DriverLocation)
elif WebBrowser == "firefox":
    driver = webdriver.Firefox(executable_path="ThePath to the geckodriver in the repo")

sel = SelHelper(driver)

#Entering the target site
driver.maximize_window()
driver.get("https://www.expedia.com/?pwaLob=wizard-hotel-pwa-v2")
driver.implicitly_wait(3)

#entering the flights tab and choosing trip type
FlightElment = sel.getElement('//*[@id="uitk-tabs-button-container"]/li[2]/a').click()
ChoseTrip = sel.getElement('//*[@id="uitk-tabs-button-container"]/div[1]//a/span[text()="%s"]//parent::*' % tripType).click()

#acting based on trip type
if tripType == "Roundtrip":
    #entering the details about the trip you want
    #filling in depart and target city's
    time.sleep(0.5)
    sel.getElement('//*[@id="location-field-leg1-origin-menu"]/div[1]/button').click()
    time.sleep(0.5)
    sel.getElement('//*[@id="location-field-leg1-origin"]').send_keys(departCity)
    time.sleep(0.5)
    sel.getElement('//*[@id="location-field-leg1-origin-menu"]/div[2]/ul/li[1]/button').click()

    time.sleep(0.5)
    sel.getElement("//div[@id='location-field-leg1-destination-menu']//button[@type='button']").click()
    time.sleep(0.5)
    sel.getElement("/html//input[@id='location-field-leg1-destination']").send_keys(targetCity)
    time.sleep(0.5)
    sel.getElement('//*[@id="location-field-leg1-destination-menu"]/div[2]/ul/li[1]/button').click()

    #filling in the dates
    sel.getElement("/html//div[@id='wizard-flight-tab-roundtrip']/div/div[2]//div[@class='uitk-flex-grow-1']/div/div[1]/div[@role='menu']/div/button[1]").click()

    #moving on till we get to the target departing month
    while sel.isElementPresent('//*[@id="wizard-flight-tab-roundtrip"]/div/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div[2]//h2[contains(text(), "%s")]' % departMonth) == False:

        forwardButton = sel.getElement("""/html//div[@id='wizard-flight-tab-roundtrip']/div/div[2]//div[@class='uitk-flex-grow-1']/div/div[1]/div[@role='menu']
        /div[@role='menuitem']//div[@class='uitk-flex uitk-flex-justify-content-space-between uitk-new-date-picker-menu-pagination-container']/button[2]""").click()
        time.sleep(0.5)

    targetDay = sel.getElement('//*[@id="wizard-flight-tab-roundtrip"]/div/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div[2]//h2[contains(text(), "%s")]//following-sibling::table//button[@data-day="%s"]' % (departMonth, departDay)).click()

    #moving on till we get to the target returning month
    while sel.isElementPresent('//*[@id="wizard-flight-tab-roundtrip"]/div/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div[2]//h2[contains(text(), "%s")]' % returnMonth) == False:

        forwardButton = sel.getElement("""/html//div[@id='wizard-flight-tab-roundtrip']/div/div[2]//div[@class='uitk-flex-grow-1']/div/div[1]/div[@role='menu']
        /div[@role='menuitem']//div[@class='uitk-flex uitk-flex-justify-content-space-between uitk-new-date-picker-menu-pagination-container']/button[2]""").click()
        time.sleep(1)

    #clicking the target day
    targetDay = sel.getElement('//*[@id="wizard-flight-tab-roundtrip"]/div/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div[2]//h2[contains(text(), "%s")]//following-sibling::table//button[@data-day="%s"]' % (returnMonth, returnDay)).click()
    
    #clicking done
    time.sleep(0.5)
    doneButton = sel.getElement('//*[@id="wizard-flight-tab-roundtrip"]/div/div[2]/div/div/div/div[1]/div/div[2]/div/div[2]/button').click()

    #serch 
    time.sleep(0.5)
    serchButton = sel.getElement('//*[@id="wizard-flight-pwa-1"]/div[3]/div[2]/button').click()

elif tripType == "One-way":
    #entering the details about the trip you want
    #filling in depart and target city's
    time.sleep(0.5)
    sel.getElement('//*[@id="location-field-leg1-origin-menu"]/div[1]/button').click()
    time.sleep(0.5)
    sel.getElement('//*[@id="location-field-leg1-origin"]').send_keys(departCity)
    time.sleep(0.5)
    sel.getElement('//*[@id="location-field-leg1-origin-menu"]/div[2]/ul/li[1]/button').click()

    time.sleep(0.5)
    sel.getElement("//div[@id='location-field-leg1-destination-menu']//button[@type='button']").click()
    time.sleep(0.5)
    sel.getElement("/html//input[@id='location-field-leg1-destination']").send_keys(targetCity)
    time.sleep(0.5)
    sel.getElement('//*[@id="location-field-leg1-destination-menu"]/div[2]/ul/li[1]/button').click()

    #filling in the dates
    sel.getElement("d1-btn", "id").click()

    #moving on till we get to the target departing month
    while sel.isElementPresent('//*[@id="wizard-flight-tab-oneway"]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]//h2[contains(text(), "%s")]' % departMonth) == False:

        forwardButton = sel.getElement("""//*[@id="wizard-flight-tab-oneway"]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[1]/button[2]""").click()
        time.sleep(1)

    #clicking the target day
    targetDay = sel.getElement('//*[@id="wizard-flight-tab-oneway"]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]//h2[contains(text(), "%s")]//following-sibling::table//button[@data-day="%s"]' % (departMonth,departDay)).click()

    #clicking done
    time.sleep(0.5)
    doneButton = sel.getElement('//*[@id="wizard-flight-tab-oneway"]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/button').click()

    #serch 
    time.sleep(0.5)
    serchButton = sel.getElement('//*[@id="wizard-flight-pwa-1"]/div[3]/div[2]/button').click()
    
elif tripType == "Multi-city":
    print("currently unavailable")