from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#To stop the web browser from auto closing
chrome_options = Options()
chrome_options.add_experimental_option("detach",True) 

#web driver initialization
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

#to open Flipkart webpage
url = 'https://www.flipkart.com'
driver.maximize_window()
driver.get(url)


#to search for books
search = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input')
search.send_keys("English Adventure story books for kids of 12 years")
search.send_keys(Keys.ENTER)


#open file to write the details of books
with open("Book Details.txt", "w", encoding="utf-8") as file:
    for k in range(1,6): #to fetch details from 5 pages
        for i in range (1,12):
            for j in range (1,5):
                try:
                    name_element = driver.find_element(By.XPATH,f'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/a[2]')
                    name = name_element.text
                    
                except:
                    name = ""
                # print("Book Name : ",name)
                
                try:
                    flipkart_price_element = driver.find_element(By.XPATH,f'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/a[3]/div/div[1]')
                    flipkart_price = flipkart_price_element.text
                except:
                    flipkart_price = ""
                # print("Flipkart Price : ", flipkart_price)

                try:
                    mrp_element = driver.find_element(By.XPATH,f'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/a[3]/div[1]/div[2]')
                    mrp = mrp_element.text
                except:
                    mrp = ""
                # print("MRP : ",mrp)

                # print("**********************************************")
                file.write(f"Book Name: {name}\n")
                file.write(f"Flipkart Price: {flipkart_price}\n")
                file.write(f"MRP: {mrp}\n")
        try:
             next = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]/span').click()
        except:
            next = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[12]/span').click()
with open("Book Details.txt", "w", encoding="utf-8") as file:
    for i in range (1,12):
            for j in range (1,5):
                try:
                    name_element = driver.find_element(By.XPATH,f'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/a[2]')
                    name = name_element.text
                    
                except:
                    name = ""
                # print("Book Name : ",name)
                
                try:
                    flipkart_price_element = driver.find_element(By.XPATH,f'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/a[3]/div/div[1]')
                    flipkart_price = flipkart_price_element.text
                except:
                    flipkart_price = ""
                # print("Flipkart Price : ", flipkart_price)

                try:
                    mrp_element = driver.find_element(By.XPATH,f'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/a[3]/div[1]/div[2]')
                    mrp = mrp_element.text
                except:
                    mrp = ""
                # print("MRP : ",mrp)

                # print("**********************************************") 
                
                file.write(f"Book Name: {name}\n")
                file.write(f"Flipkart Price: {flipkart_price}\n")
                file.write(f"MRP: {mrp}\n")  
                
driver.quit()