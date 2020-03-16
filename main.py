from selenium import webdriver
from time import sleep


class SteamBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login_phase(self):
        self.driver.get("https://steamcommunity.com/login/home")
        steam_username = self.driver.find_element_by_xpath("""//*[@id="steamAccountName"]""")
        steam_username.send_keys("yourEmail@domain.com")
        steam_password = self.driver.find_element_by_xpath("""//*[@id="steamPassword"]""")
        steam_password.send_keys("yourPassword")
        login_button = self.driver.find_element_by_xpath("""//*[@id="SteamLogin"]""")
        login_button.click()

    def change_name(self):
        name_list = ["add","me","on","discord","darius#6666"]
        name = self.driver.find_element_by_xpath("""//*[@id="editForm"]/div[10]/div/button""")
        for i in(name_list):

            toClear = self.driver.find_element_by_xpath("""//*[@id="personaName"]""")
            toClear.clear()

            #Send name
            c = i
            name = self.driver.find_element_by_xpath("""//*[@id="personaName"]""")
            name.send_keys(c)
            
            # Save Changes
            save_change = self.driver.find_element_by_xpath("""//*[@id="editForm"]/div[10]/div/button""")
            save_change.click()
            sleep (5)

    def welcome_message(self):
        print ("This is a Steam Nickname Changer, which is automated!")
        print ("This is V.1.0, currently it will run forever until you use Ctrl + C to stop it.")
        print ("Future updates include: Background run, better UI, take input")

bot = SteamBot()
bot.login_phase()
bot.welcome_message()
a = True
stop = False
while a == True:
    ready = input("Are you ready? [Y]es or [N]o").lower()
    if ready == ("y"):
        while True:
            bot.change_name()
    
