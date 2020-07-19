from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys

#line 98: Input your username and password
#line 25: after the '/tags' text, type in the hastag you want to promote yourself in 
#line 33: in between the " ", type in the comment that you want to comment in each post
#line 53: this is the amount of time that will be delayed in each post before going on to the next one. I reccomend having at least a minute of delay to avoid instgram bans
#line 103: type in the number of posts you want to engage in. I reccoment staying below 60 to avoid instagram bans 

def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstagramBot:
    def GetHashtag(self):
        time.sleep(3)
        print("success")
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/unsignedartist/") #choose your hashtag where you want to market
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        

    def run(self, amount):

        driver = self.driver
        post_without_comment = 0
        text = "Offering music marketing services: Industry label contacts, exclusive beat bundles for a dollar each, full music management services, and more. Go follow us!"
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        driver.find_element_by_class_name('v1Nh3').click()

        j = 1
        while j <= 10:
            time.sleep(0.5)
            driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            j += 1

        i = 1
        while i <= amount:
            try:
                time.sleep(1)
                driver.find_element_by_class_name('fr66n').click() #like button
                time.sleep(5)
                driver.find_element_by_class_name('Ypffh').click()
                driver.find_element_by_class_name('Ypffh').send_keys(text)
                driver.find_element_by_class_name('Ypffh').send_keys(Keys.RETURN)
                time.sleep(90)
                driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click() #nextslide 
                i += 1
                print(i)
            except Exception:
                print("This dude has no commenting")
                driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
                post_without_comment += 1
                

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
 
    def closeBrowser(self):
        self.driver.close()
                   
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def nav_user(self, user):
        self.driver.get('{}/{}'.format(self.base_url), user)


if __name__ == "__main__":

    username = "USERNAME"
    password = "PASSWORD"
    
    

    ig = InstagramBot("lemonaderecords22", "Stevecraftpro2") 
    ig.login() # Goes to the 'def login' part
    time.sleep(2)
    
    ig.GetHashtag()
    ig.run(60)