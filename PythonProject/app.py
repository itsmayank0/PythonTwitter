from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self, username, passward):
        self.username = username
        self.passward = passward
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com')
        time.sleep(7)
        email = bot.find_element_by_class_name("email-input")
        password = bot.find_element_by_name("session[password]")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        time.sleep(3)
        password.send_keys(self.passward)
        password.send_keys(Keys.RETURN)
        time.sleep(5)
 #For liking the tweets one by one
    def like_t(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(14)

        #Change the value 2 to anything according to your time preference.
        for i in range(0,2):
            bot.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(9)
            tws = bot.find_elements_by_class_name('tweet')
            links = [ elm.get_attribute('data-permalink-path') for elm in tws ]
            #print(links)
            for link in links:
                bot.get('https://twitter.com/'+link)
                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(30)
                except Exception as e:
                    time.sleep(60)
"""***Step 1:  In the method TwitterBot, give your registered Email and password.
      Step 2:  Give Hashtag in like_t method (hashtag or search for releted tweets)
      Step 3:  Change the value 2 to anything according to your time preference.
"""


obj = TwitterBot('xyz@gmail.com','password')
obj.login()
obj.like_t("gurupurnima")
