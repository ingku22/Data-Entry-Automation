
# Data Entry Automation Project

This project aims to create an application that allows new merchants to upload images, crop these images and generate a curated excel file for data entry/merchant onboarding automation.





## Features

- Easy and Intuitive Design without needed tutorial
- Simple Navigatable Menu bar
- Cropping Toolkit
- User-friendly Automation
- Simple Error Handling



## Installation (Developer)

1. Install data entry automation project with git clone

```bash
  git clone https://github.com/ingku22/Data-Entry-Automation.git
```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Installation (User)

1. Obtain the .exe file, click the .exe file to activate the tkinter application front end. 

[Refer to Deployment](#Deployment)



    
## Usage

1. Upload an image from local file system to display on the application in the right size.
2. Crop the uploaded image by its category portion.
3. Compile the cropped image into a directory by its category name and export as a directory of images
4. Upload the image directory for reading by an OCR model to obtain Excel file
5. Upload Excel file to begin Automation



## Requirements

To run this project, you will need to have the following modules/clients

`google browser > 115.00.00`

`pillow == 10.2.0`

`pandas == 2.1.2`

`numpy == 1.26.4`

`easyocr == 1.7.1`

`selenium == 4.18.1`

`openpyxl == 3.1.2`

PS. If there is an error with selenium, do check if the google browser version is 
compatible with the chromedriver located in 
`env/Lib/selenium/chromedriver`


## Deployment

Project has been intended to be deployed as a .exe file via the use of pyinstaller using the following command

```bash
  pyinstaller -w --onefile
--add-data "final_product/assets;assets"
--add-data "final_product/pages;pages"
--add-data "final_product/preprocess.json;."
final_product/main.py
```

#### Current Versions ***(WIP)
- version 0.0.1 (not in use)







## Road Map

#### Tkinter FrontEnd
- [ ] Update image filetype compatibility
- [ ] Tweak bugs that causes cropping corruption
- [ ] Implement Image manupilation (zoom in out, rotate)
- [ ] Implement Settings for automation customization



#### OCR Handling
- [ ] Implement error handling and edge cases.
- [ ] Improve user interface with better feedback and instructions.
- [ ] Add support for additional OCR libraries.
- [ ] Enhance cropping functionality for better accuracy. 


#### Excel Handling
- [ ] Improve Classification algorithm from OCR result
- [ ] Implement Excel Format Validation

#### Automation
--- Completed ---

## Acknowledgements

 - [Tkinter Designer Generator (Figma -> Tkinter)](https://github.com/ParthJadhav/Tkinter-Designer/tree/master)
 - [README editor](https://readme.so/editor)
