import browser
import insta_elements
import insta_endpoints

class Login_user:
    def __init__(self, driver, username, password, cookie):
        self.username = username
        self.password = password
        self.cookie = cookie