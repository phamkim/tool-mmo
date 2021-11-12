
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Gmail:
    userName: str = ''

    def __init__(self, _userName):
        self.userName = _userName

    def checkUserName(seft):
        options = webdriver.ChromeOptions()
        options.headless = True
        try:
            driver = webdriver.Chrome(
                ChromeDriverManager().install(), options=options)
            driver.set_window_size(width=500, height=700)
            driver.get('https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=SignUp')
            driver.implicitly_wait(5)
            loginBox = driver.find_element_by_xpath('//*[@id ="username"]')
            loginBox.send_keys(seft.userName)
            nextButton = driver.find_elements_by_xpath(
                '//*[@id ="headingSubtext"]')
            nextButton[0].click()
            isOk = driver.find_elements_by_xpath("//*[@class='o6cuMc']")
            if(isOk):
                return False
            else:
                return True
        except:
            return False
