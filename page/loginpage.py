from common.basepage import BasePage
import time
from common.log import Log


class LoginPage(BasePage):

    def link_login_page(self, website='com'):
        if website.upper() == 'COM':
            self.link_page("https://www.multilotto.com/en/user/signin")
        elif website.upper() == 'NET':
            self.link_page("https://www.multilotto.net/en/user/signin")
        elif website.upper() == "IE":
            self.link_page("https://www.multilotto.ie/en/user/signin")
        elif website.upper() == "COUK" or "CO.UK":
            self.link_page("https://www.multilotto.co.uk/en/user/signin")
        else:
            self.link_page("https://www.multilotto.com/en/user/signin")

    def login(self, username, password):
        self.driver.find_element("用户名输入框").clear()
        self.driver.find_element("用户名输入框").send_keys(username)
        self.driver.find_element("密码输入框").clear()
        self.driver.find_element("密码输入框").send_keys(password)
        self.driver.find_element("登录提交按钮").click()

    def is_login_sucess(self):
        current_title = self.get_current_title()
        current_url = self.get_current_url()
        if ("user/dashboard" or "user/deposit/") in current_url and "Online Lottery" in current_title:
            Log().info("登录成功，当前的地址为：" + current_url)
            return True
        Log().error("登录失败，请检查")
        return False


if __name__ == '__main__':
    lp = LoginPage()
    lp.link_login_page()
    lp.close_age_alert()
    lp.login("cai.wenjuan+test4@themultigroup.com", "MMMmmm500")
    time.sleep(10)
    print(lp.is_login_sucess())
    lp.close_current_page()
