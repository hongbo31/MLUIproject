from common.drive import Drive


class BasePage:

    def __init__(self, web=1):
        self.current_page = None
        self.driver = Drive(web)

    # 进入页面，传入url地址
    def link_page(self, url, needmaxwindow=True):
        self.driver.open_browser(url, needmaxwindow)

    # 页面前进
    def forward_page(self):
        self.driver.forward()

    # 页面回退
    def back_page(self):
        self.driver.back()

    # 返回当前页面的url
    def get_current_url(self):
        return self.driver.driver.current_url

    # 返回当前页面的title
    def get_current_title(self):
        return self.driver.driver.title

    # 获取当前窗口的handle
    def get_current_window_handle(self):
        return self.driver.driver.current_window_handles

    # 获取所有窗口的handle
    def get_windows_handles(self):
        return self.driver.driver.window_handles

    # 跳转到iframe页面， 可传参数name，id，如果iframe没有这个属性的话，可以用index或者element来定位
    def switch_to_iframe(self):
        self.driver.driver.switch_to.frame()

    # 回到原来的iframe页面
    def switch_to_back_default_iframe(self):
        self.driver.driver.switch_to.default_content()

    # 首页出现18岁年龄确认弹窗，关闭弹窗
    def close_age_alert(self):
        self.driver.find_element("首页年龄弹窗确认").click()

    def close_current_page(self):
        self.driver.close_browser()


if __name__ == '__main__':
    page = BasePage()
   # page.driver.open_browser("http://www.multilotto.com/en")
  #  page.driver.find_element("首页弹窗确认").click()
    page.link_page("首页登录按钮", False)


