from common.basepage import BasePage

class HomePage(BasePage):

    # 进入网站首页，传入站点名称即可 (如com、net、ie、couk/co.uk)
    def link_home_page(self, website='com'):
        if website.upper() == 'COM':
            self.link_page("https://www.multilotto.com/en")
        elif website.upper() == 'NET':
            self.link_page("https://www.multilotto.net/en")
        elif website.upper() == "IE":
            self.link_page("https://www.multilotto.ie/en")
        elif website.upper() == "COUK" or "CO.UK":
            self.link_page("https://www.multilotto.co.uk/en")
        else:
            self.link_page("https://www.multilotto.com/en")

    # 点击首页左上角的logo，刷新页面
    def refresh_page(self):
        self.driver.find_element("首页图标").click()

    # 从首页进入登录页面
    def link_signin_page(self):
        self.driver.find_element("首页signin按钮").click()

    def link_signup_page(self):
        self.driver.find_element("首页signup按钮").click()



homepg = HomePage()
homepg.link_home_page('net')

