from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def main():
    options = Options()
    options.add_experimental_option("detach", True)

    #driver = webdriver.Chrome(service=driver_service,options=options)
    service_obj = Service("/home/chawas/.wdm/drivers/chromedriver/linux64/128.0.6613.119/chromedriver-linux64/chromedriver")
    driver = webdriver.Chrome(service=service_obj, options=options)
    
    driver.get("https://wchawaguta.com/miscellaneous/a-lighter-look/")
    driver.maximize_window()

    driver.find_element(By.XPATH, "//*[@id='pwbox-416']").send_keys("Chawazi2020\\")

    driver.find_element(By.XPATH, "//*[@id='wp--skip-link--target']/div[2]/form/p[2]/input").click()

main()
