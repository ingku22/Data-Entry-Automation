## chromedriver update is managed by selenium-manager, to access existing browser
## run chrome debugger on port 9222: "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 

from pathlib import Path
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By     
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


def automation_process(file_path):

    if (file_path):
        print("Running...") 

        menuDF = pd.read_excel(file_path, sheet_name=0)
        menuDF = menuDF[menuDF["ItemID"].notna()]

        ### Loading up driver options

        options = webdriver.ChromeOptions() 
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222") # To allow Selenium to connect to existing browser, need to run browser debugger on port 9222
        driver = webdriver.Chrome(options=options) 
        wait = WebDriverWait(driver, timeout = 5)

        driver.get("https://queuecuts.com:444/YourStore/EditStore")

        ### Automate creation of menu

        menuBtnXPath = "//main[1]//div[1]//a[2]" # Change according to html 
        menuInputID = "menu_Name"
        menuDescID = "menu_Description"

        menuBtn = driver.find_element(By.XPATH, menuBtnXPath)
        menuBtn.click()

        # menuInput = driver.find_element(By.ID, menuInputID)
        # menuDesc = driver.find_element(By.ID, menuDescID)
        # wait.until(lambda d: menuInput.is_displayed())

        # menuInput.send_keys("Menu")
        # menuDesc.send_keys("-")

        # menuSubmit = driver.find_element(By.TAG_NAME, "form").find_element(By.TAG_NAME, "button")
        # menuSubmit.click()

        ## Automate uploading of food items

        addCatBtnDivID = "foodTable"
        foodNameInputID = "food_Name"
        foodCategoryInputID = "food_Category"
        foodPriceInputID = "food_Start_Price"
        foodTakeawayInputID = "food_Takeaway_Fee"
        foodPrepareInputID = "food_Prepare_Time"
        foodDescInputID = "food_Description"
        submitBtnXPath = "//button[@type='submit']"
        menuBackBtnXPath = "//form//a[1]"

        for index in menuDF.index:
            AddCatBtn = driver.find_element(By.ID, addCatBtnDivID).find_element(By.XPATH, "(//a)[last()]")
            ActionChains(driver).move_to_element(AddCatBtn).perform()
            wait.until(lambda d: AddCatBtn.is_displayed())
            AddCatBtn.click()

            foodNameInput = driver.find_element(By.ID, foodNameInputID)
            foodCategoryInput = driver.find_element(By.ID, foodCategoryInputID)
            foodPriceInput = driver.find_element(By.ID, foodPriceInputID)
            foodTakeawayInput = driver.find_element(By.ID, foodTakeawayInputID)
            foodPrepareInput = driver.find_element(By.ID, foodPrepareInputID)
            foodDescInput = driver.find_element(By.ID, foodDescInputID)
            submitBtn = driver.find_element(By.XPATH, submitBtnXPath)
        
            data = [menuDF["Menu Items"][index], menuDF["Category"][index], menuDF["Costs"][index], 0, 15, menuDF["Description"][index]]
            foodNameInput.send_keys(data.pop(0))
            foodCategoryInput.send_keys(data.pop(0))
            foodPriceInput.send_keys(data.pop(0))
            foodTakeawayInput.send_keys(data.pop(0))
            foodPrepareInput.send_keys(data.pop(0))
            foodDescInput.send_keys(data.pop(0))

            ActionChains(driver).move_to_element(submitBtn).perform()
            wait.until(lambda d: submitBtn.is_displayed())
            submitBtn.click()

            menuBackBtn = driver.find_element(By.XPATH, menuBackBtnXPath)
            wait.until(lambda d: menuBackBtn.is_displayed())
            menuBackBtn.click()

        ### Automate uploading of option groups

        optionGrpDF = pd.read_excel(file_path, sheet_name=2)
        optionGrpDF = optionGrpDF[optionGrpDF["GroupID"].notna()]


        optionGrpBtnXPath = "//main//ul//li[2]//a"
        addOptionGrpBtnXPath = "//a[@href='/Menu/AddOptionGroup']"
        groupNameInputID = "opt_Grp_Name"   
        optionGrpTypeID = "opt_Grp_Type"
        optionGrpMandID = "opt_Grp_IsMandatory"
        createBtnXPath = "//form//button"
        addOptionBtnXPath = "//a[contains(@href, '/Menu/AddNewOption')]"


        optionGrpBtn = driver.find_element(By.XPATH, optionGrpBtnXPath)
        wait.until(lambda d: optionGrpBtn.is_displayed())
        optionGrpBtn.click()

        for index in optionGrpDF.index:
            addOptionGrpBtn = driver.find_element(By.XPATH, addOptionGrpBtnXPath)
            ActionChains(driver).move_to_element(addOptionGrpBtn).perform()
            wait.until(lambda d: addOptionGrpBtn.is_displayed())
            addOptionGrpBtn.click()

            groupNameInput = driver.find_element(By.ID, groupNameInputID)
            optionGrpType = Select(driver.find_element(By.ID, optionGrpTypeID))
            optionGrpMand = driver.find_element(By.ID, optionGrpMandID)
            createBtn = driver.find_element(By.XPATH, createBtnXPath)

            data = {
                "GroupName": optionGrpDF["GroupName"][index],
                "DropDown": optionGrpDF["DropDown"][index],
                "Mandatory": optionGrpDF["Mandatory"][index]
                }

            groupNameInput.send_keys(data["GroupName"])
            if (data["DropDown"]):
                optionGrpType.select_by_visible_text("Checkbox")
            if(data["Mandatory"]):
                optionGrpMand.click()
            createBtn.click()

            ## Automate uploading of add-on Options

            linkedOptionsDF = pd.read_excel(file_path, sheet_name=3)
            linkedOptionsDF = linkedOptionsDF[linkedOptionsDF["GroupID"].notna()]

            optionsDF = pd.read_excel(file_path, sheet_name=4)
            optionsDF = optionsDF[optionsDF["OptionID"].notna()]

            optionID = linkedOptionsDF.loc[linkedOptionsDF['GroupID'] == index]["OptionID"]
            optionID = np.array(optionID)

            createdOptionGrpXPath = f"//div[@class='accordion-header'][{index + 1}]//a"

            createdOptionGrp = driver.find_element(By.XPATH, createdOptionGrpXPath)
            ActionChains(driver).move_to_element(createdOptionGrp).perform()
            wait.until(lambda d: createdOptionGrp.is_displayed())
            createdOptionGrp.click()

            for i in optionID:

                row = optionsDF[optionsDF["OptionID"] == i]
                data = {"OptionTitle": row.iloc[0]["OptionTitle"],
                        "OptionVal": row.iloc[0]["OptionVal"]}
                
                addOptionBtn = driver.find_element(By.XPATH, addOptionBtnXPath)
                ActionChains(driver).move_to_element(addOptionBtn).perform()
                wait.until(lambda d: addOptionBtn.is_displayed())
                addOptionBtn.click()

                optionNameInputID = "opt_Unit"
                optionPriceInputID = "opt_Price"
                submitOptionBtnXPath = "//button[@type='submit']"

                optionNameInput = driver.find_element(By.ID, optionNameInputID)
                optionPriceInput = driver.find_element(By.ID, optionPriceInputID)
                submitOptionBtn = driver.find_element(By.XPATH, submitOptionBtnXPath)

                wait.until(lambda d: optionNameInput.is_displayed())
                optionNameInput.send_keys(data["OptionTitle"])
                optionPriceInput.send_keys(data["OptionVal"])
                submitOptionBtn.click()

            ## Automate Linking Dish to Option
                
            linkedDishDF = pd.read_excel(file_path, sheet_name=1)
            linkedDishDF = linkedDishDF[linkedDishDF["GroupID"].notna()]
            itemID = linkedDishDF.loc[linkedDishDF['GroupID'] == index]["ItemID"]
            itemID = np.array(itemID)

            addLinkedDishBtnXPath = "//a[contains(@href, '/Menu/LinkedDish')]"
            optionGrpBackBtnXPath = "//a[contains(@href, 'Menu/OptionGroups')]"

            addLinkedDishBtn = driver.find_element(By.XPATH, addLinkedDishBtnXPath)
            ActionChains(driver).move_to_element(addLinkedDishBtn).perform()
            wait.until(lambda d: addLinkedDishBtn.is_displayed())
            addLinkedDishBtn.click()

            submitLinkedDishBtnXPath = "//button[@type='submit']"

            for i in itemID:
                name = menuDF[menuDF["ItemID"] == i].iloc[0]["Menu Items"]

                itemNameXPATH = f"//div[contains(text(), '{name}')]//input"

                itemName = driver.find_element(By.XPATH, itemNameXPATH)
                ActionChains(driver).move_to_element(itemName).perform()
                wait.until(lambda d: itemName.is_displayed())
                itemName.click()

            submitLinkedDishBtn = driver.find_element(By.XPATH, submitLinkedDishBtnXPath)
            ActionChains(driver).move_to_element(submitLinkedDishBtn).perform()
            wait.until(lambda d: submitLinkedDishBtn.is_displayed())
            submitLinkedDishBtn.click()

            optionGrpBackBtn = driver.find_element(By.XPATH, optionGrpBackBtnXPath)
            wait.until(lambda d: optionGrpBackBtn.is_displayed())
            optionGrpBackBtn.click()
        