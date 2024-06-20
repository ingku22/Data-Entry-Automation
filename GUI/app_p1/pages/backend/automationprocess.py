import time
import os
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from tkinter import messagebox
import tkinter as tk
import pandas as pd

def create_input(excelPath):

    def submit():
        email = email_entry.get()
        password = password_entry.get()
        store = storeName_entry.get()
        root.destroy()
        automation_process(email, password, store, excelPath)


    # Create the main window
    root = tk.Tk()
    root.geometry("600x200")

    email_label = tk.Label(root, text="Enter email:")
    email_label.pack()

    # Create an entry widget for input
    email_entry = tk.Entry(root, width=60)
    email_entry.pack()

    password_label = tk.Label(root, text="Enter password")
    password_label.pack()

    # Create an entry widget for input
    password_entry = tk.Entry(root, width=60)
    password_entry.pack()

    store_label = tk.Label(root, text="Enter merchant portal store name")
    store_label.pack()

    # Create an entry widget for input
    storeName_entry = tk.Entry(root, width=60)
    storeName_entry.pack()

    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.pack()

    root.mainloop()

def automation_process(email, password, storeName, excelPath):
    try:
        itemDF = pd.read_excel(excelPath, sheet_name=0)
        itemDF = itemDF[itemDF["Menu Item"].notna()]

        ### Loading up driver options

        options = webdriver.ChromeOptions() 
        driver = webdriver.Chrome(options=options) 
        driver.maximize_window()
        wait = WebDriverWait(driver, timeout = 5)

        driver.get("https://queuecuts.com:444")

        emailInputID = "Email"
        passwordInputID = "id_password"
        submitBtnXPath = "//button[@type='submit']"

        emailInput = driver.find_element(By.ID, emailInputID)
        passwordInput = driver.find_element(By.ID, passwordInputID)
        submitBtn = driver.find_element(By.XPATH, submitBtnXPath)

        wait.until(lambda d: submitBtn.is_displayed())
        emailInput.send_keys(email)
        passwordInput.send_keys(password)
        submitBtn.click()

        storeSelectID = "selectStore"

        storeSelect = Select(driver.find_element(By.ID, storeSelectID))
        storeSelect.select_by_visible_text(storeName)

        driver.get("https://queuecuts.com:444/YourStore/EditStore")

        ### Automate creation of menu

        menuBtnXPath = "//main[1]//div[1]//a[2]" # Change according to html 
        menuInputID = "menu_Name"
        menuDescID = "menu_Description"

        menuBtn = driver.find_element(By.XPATH, menuBtnXPath) 
        menuBtn.click()

        menuInput = driver.find_element(By.ID, menuInputID)
        if menuInput.is_displayed():
            menuDesc = driver.find_element(By.ID, menuDescID)
            wait.until(lambda d: menuInput.is_displayed())

            menuInput.send_keys("Menu")
            menuDesc.send_keys("-")

            menuSubmit = driver.find_element(By.TAG_NAME, "form").find_element(By.TAG_NAME, "button")
            menuSubmit.click()
        else:
            print("Menu already created")

        # Automate uploading of food items

        addCatBtnDivID = "foodTable"
        foodNameInputID = "food_Name"
        foodCategoryInputID = "food_Category"
        foodPriceInputID = "food_Start_Price"
        foodTakeawayInputID = "food_Takeaway_Fee"
        foodPrepareInputID = "food_Prepare_Time"
        foodDescInputID = "food_Description"
        submitBtnXPath = "//button[@type='submit']"
        menuBackBtnXPath = "//form//a[1]"

        for index in itemDF.index:
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

            foodNameInput.send_keys(itemDF["Menu Item"][index])
            foodCategoryInput.send_keys(itemDF["Category"][index])
            foodPriceInput.send_keys(itemDF["Costs"][index])
            foodTakeawayInput.send_keys(0) # PLACEHOLDER
            foodPrepareInput.send_keys(15) # PLACEHOLDER
            foodDescInput.send_keys(itemDF["Description"][index])

            ActionChains(driver).move_to_element(submitBtn).perform()
            wait.until(lambda d: submitBtn.is_displayed())
            submitBtn.click()

            menuBackBtn = driver.find_element(By.XPATH, menuBackBtnXPath)
            wait.until(lambda d: menuBackBtn.is_displayed())
            menuBackBtn.click()

        # Automate uploading of option groups

        optionData = {}

        optionGrpDF = pd.read_excel(excelPath, sheet_name=1)
        optionGrpDF = optionGrpDF[optionGrpDF["Option Groups"].notna()]

        optionDF = pd.read_excel(excelPath, sheet_name=2)
        optionDF = optionDF[optionDF["Option Group"].notna()]

        optionGrpNames = list(optionGrpDF["Option Groups"])

        for optionGrpName in optionGrpNames:
            optionGrpType = optionGrpDF[optionGrpDF["Option Groups"] == optionGrpName]["Single"].values[0]
            optionGrpMand = optionGrpDF[optionGrpDF["Option Groups"] == optionGrpName]["Mandatory"].values[0]
            optionNames = list(optionDF[optionDF["Option Group"] == optionGrpName]["Option"])
            optionCosts = list(optionDF[optionDF["Option Group"] == optionGrpName]["Cost"])
            optionData[optionGrpName] = [optionGrpType, optionGrpMand, optionNames, optionCosts]

        optionGrpBtnXPath = "//main//ul//li[2]//a"
        addOptionGrpBtnXPath = "//a[@href='/Menu/AddOptionGroup']"
        groupNameInputID = "opt_Grp_Name"   
        optionGrpTypeID = "opt_Grp_Type"
        optionGrpMandID = "opt_Grp_IsMandatory"
        optionMinInputID = "opt_Grp_Min"
        optionMaxInputID = "opt_Grp_Max"
        createBtnXPath = "//form//button"
        addOptionBtnXPath = "//a[contains(@href, '/Menu/AddNewOption')]"


        optionGrpBtn = driver.find_element(By.XPATH, optionGrpBtnXPath)
        wait.until(lambda d: optionGrpBtn.is_displayed())
        optionGrpBtn.click()

        for optionGrp in optionData:
            addOptionGrpBtn = driver.find_element(By.XPATH, addOptionGrpBtnXPath)
            ActionChains(driver).move_to_element(addOptionGrpBtn).perform()
            wait.until(lambda d: addOptionGrpBtn.is_displayed())
            addOptionGrpBtn.click() 

            groupNameInput = driver.find_element(By.ID, groupNameInputID)
            optionGrpType = Select(driver.find_element(By.ID, optionGrpTypeID))
            optionGrpMand = driver.find_element(By.ID, optionGrpMandID)
            optionMinInput = driver.find_element(By.ID, optionMinInputID)
            optionMaxInput = driver.find_element(By.ID, optionMaxInputID)
            createBtn = driver.find_element(By.XPATH, createBtnXPath)

            data = {
                "GroupName": optionGrp,
                "DropDown": optionData[optionGrp][0],
                "Mandatory": optionData[optionGrp][1],
                "OptionNames": optionData[optionGrp][2],
                "OptionPrices": optionData[optionGrp][3]
                }

            print(data)
            

            groupNameInput.send_keys(data["GroupName"])
            if (data["DropDown"]):
                optionGrpType.select_by_visible_text("Checkbox")
            if (data["Mandatory"]):
                optionGrpMand.click()
            createBtn.click()

        ## Automate uploading of add-on Options``

            createdOptionGrpXPath = f"//div[@class='accordion-header']//a[contains(text(), '{data['GroupName']}')]"

            createdOptionGrp = driver.find_element(By.XPATH, createdOptionGrpXPath)
            ActionChains(driver).move_to_element(createdOptionGrp).perform()
            wait.until(lambda d: createdOptionGrp.is_displayed())
            createdOptionGrp.click()

            for i in range(len(data["OptionNames"])):
                addOptionBtn = driver.find_element(By.XPATH, addOptionBtnXPath)
                ActionChains(driver).move_to_element(addOptionBtn).perform()
                wait.until(lambda d: addOptionBtn.is_displayed())
                try:
                    addOptionBtn.click()
                except:
                    time.sleep(2)
                    addOptionBtn.click()

                optionNameInputID = "opt_Unit"
                optionPriceInputID = "opt_Price"
                submitOptionBtnXPath = "//button[@type='submit']"

                optionNameInput = driver.find_element(By.ID, optionNameInputID)
                optionPriceInput = driver.find_element(By.ID, optionPriceInputID)
                submitOptionBtn = driver.find_element(By.XPATH, submitOptionBtnXPath)

                wait.until(lambda d: optionNameInput.is_displayed())
                optionNameInput.send_keys(data["OptionNames"][i])
                optionPriceInput.send_keys(data["OptionPrices"][i])
                submitOptionBtn.click()

            ## Automate Linking Dish to Option

            addLinkedDishBtnXPath = "//a[contains(@href, '/Menu/LinkedDish')]"
            optionGrpBackBtnXPath = "//a[contains(@href, 'Menu/OptionGroups')]"

            addLinkedDishBtn = driver.find_element(By.XPATH, addLinkedDishBtnXPath)
            ActionChains(driver).move_to_element(addLinkedDishBtn).perform()
            wait.until(lambda d: addLinkedDishBtn.is_displayed())
            addLinkedDishBtn.click()

            submitLinkedDishBtnXPath = "//button[@type='submit']"

            names = []

            for index, row in itemDF[itemDF["Option Groups"].notna()].iterrows():
                if data["GroupName"] in row['Option Groups']:
                    names.append(row["Menu Item"])

            for name in names:
                
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

        return messagebox.showinfo(title='Success',
                                   message='Uploading has completed without any errors.')

    except NoSuchElementException as e:
        driver.close()
        return messagebox.showerror(title='NoSuchElementException',
                                    message=f'Please ensure that the email, password, and store name typed are correct.')
    
    except TimeoutException as e: 
        driver.close()
        return messagebox.showerror(title='TimeoutException',
                                    message=f'Program timed out. Please try again.')

    except Exception as e:
        driver.close()
        return messagebox.showerror(title='Exception',
                                    message=f'{e}')

    

