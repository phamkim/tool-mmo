
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Tool:
    listUserName = []

    def __init__(self, _listUserName):
        self.listUserName = list(_listUserName)

    def checkGmail(seft):
        listOk = list()
        options = webdriver.ChromeOptions()
        options.headless = True
        try:
            driver = webdriver.Chrome(
                ChromeDriverManager().install(), options=options)
            driver.get(
                'https://accounts.google.com/signup/v2/webcreateaccount?flowEntry=SignUp&flowName=GlifWebSignIn')     
            driver.implicitly_wait(5)
            print('on '+driver.title)
            for userName in seft.listUserName:
          
                input = driver.find_element_by_xpath('//*[@id ="username"]')
                input.clear()
                input.send_keys(userName)
                print(userName)
                nextButton = driver.find_elements_by_xpath(
                    '//*[@id ="headingSubtext"]')
                nextButton[0].click()
                isOk = driver.find_elements_by_xpath("//*[@class='o6cuMc']")
                if not isOk:
                    listOk.append(userName)
            return listOk
        except:
            return listOk

    def checkYahoo(seft):
        listOk = list()
        options = webdriver.ChromeOptions()
        options.headless = True
        try:
            driver = webdriver.Chrome(
                ChromeDriverManager().install(), options=options)
            driver.get('https://login.yahoo.com/account/create') 
            driver.implicitly_wait(5)
            print('on '+driver.title)
            for userName in seft.listUserName:
                input = driver.find_element_by_xpath(
                    '//*[@id ="usernamereg-yid"]')
                input.clear()
                input.send_keys(userName)
                print(userName)
                nextButton = driver.find_elements_by_xpath(
                    '//*[@id ="usernamereg-password"]')
                nextButton[0].click()
                isOk = driver.find_elements_by_xpath(
                    "//*[@class='oneid-error-message']")
                if not isOk:
                    listOk.append(userName)
            return listOk
        except:
            return listOk
