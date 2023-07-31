from UserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# chromedriver = r"C:\Users\kdrer\Downloads\chromedriver"

# class Ig:
#     def __init__(self, username, password):
#         self.browser = webdriver.Chrome(chromedriver)
        
#         self.username = username
#         self.password = password

#     def signIn(self):
#         self.browser.get("https://www.instagram.com/")
#         time.sleep(4)

#         usernameInput = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
#         passwordInput = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")

#         usernameInput.send_keys(self.username)
#         passwordInput.send_keys(self.password)
#         passwordInput.send_keys(Keys.ENTER)

#         time.sleep(5)
#         # aşağıdaki de çalışıyor.
#         # self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]").click()
#         # time.sleep(2)
    
#     def getFollowers(self):
#         # self.browser.get(f"https://www.instagram.com/{self.username}")
#         self.browser.get("https://www.instagram.com/eymenpatik")
#         time.sleep(2)
#         self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[2]/a/div").click()
#         time.sleep(6)
#         self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[2]/div/div/a").click()
#         time.sleep(6)
        
#         # dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
#         # followerCount = len(dialog.find_elements_by_xpath("//a[@class='FPmhX notranslate TlrDj']"))

#         # print(f"first count: {followerCount}")

#         # action = webdriver.ActionChains(self.browser)

#         # while True:
#         #     dialog.click()
#         #     action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
#         #     time.sleep(5)

#         #     newCount = len(dialog.find_elements_by_css_selector("li"))

#         #     if followerCount != newCount:
#         #         followerCount = newCount
#         #         print(f"second count: {newCount}")
#         #         time.sleep(2)
#         #     else:
#         #         break
        
#         followers = document.getElementsByClassName('_1XyCr')[0].lastElementChild.click()

#         followerList = []
#         i = 0
#         for user in followers:
#             link = user.find_element_by_css_selector("a").get_attribute("href")            
#             followerList.append(link)            
#             i += 1
#             if i == max:
#                 break

#         with open("followers.txt", "w",encoding="UTF-8") as file:
#             for item in followerList:
#                 file.write(item + "\n")


    

# ig = Ig(username, password)
# ig.signIn()
# ig.getFollowers()



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = r"C:\Users\kdrer\Downloads\chromedriver"

class InstagramBot():
    def __init__(self, email, password):
         self.browser = webdriver.Chrome(chromedriver)
         self.username = username
         self.password = password
        
        

    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(4)

        usernameInput = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)

        time.sleep(5)

     
    def getUserFollowers(self, username, max):
        self.browser.get('https://www.instagram.com/' + username)
        followersLink = self.browser.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(2)
        followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
    
        followersList.click()
        actionChain = webdriver.ActionChains(self.browser)
        while (numberOfFollowersInList < max):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)
        
        followers = []
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            print(userLink)
            followers.append(userLink)
            if (len(followers) == max):
                break
        return followers



bot = InstagramBot('cekilis_bot', '159753a')
bot.signIn()
print(bot.getUserFollowers('eymenpatik', '30'))