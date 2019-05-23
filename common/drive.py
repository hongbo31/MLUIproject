from selenium import webdriver
from common.elementRead import ElementsRead
from selenium.webdriver.common.action_chains import ActionChains
import time


class Drive:
    def __init__(self, web=1):
        self.elementRead = ElementsRead()
        if web == 1:
            self.driver = webdriver.Chrome()
        elif web == 2:
            self.driver = webdriver.Firefox()
        elif web == 3:
            self.driver = webdriver.Ie()
        self.action = ActionChains(self.driver)

    def open_browser(self, url):
        #self.driver.maximize_window()
        self.driver.get(url)
        return self.driver

    # def maximize_window(self):
    #     self.driver.maximize_window()
    #     return self.driver

    def getwindow_size(self):
        self.driver.get_window_size()

    def setwindow_size(self, width, height, windowHandle='current'):
        self.driver.set_window_size(width, height, windowHandle)

    def close_browser(self):
        self.driver.quit()

    def find_element(self, name=None):
        pathType = self.elementRead.getPathType(name)
        pathValue = self.elementRead.getPathValue(name)
        if pathType.lower() == 'id':
            return self.driver.find_element_by_id(pathValue)
        elif pathType.lower() == 'class_name':
            return self.driver.find_element_by_class_name(pathValue)
        elif pathType.lower() == 'name':
            return self.driver.find_element_by_name(pathValue)
        elif pathType.lower() == 'css_selector':
            return self.driver.find_element_by_css_selector(pathValue)
        elif pathType.lower() == 'xpath':
            return self.driver.find_element_by_xpath(pathValue)
        elif pathType.lower() == 'link_text':
            return self.driver.find_element_by_link_text(pathValue)
        elif pathType.lower() == 'tag_name':
            return self.driver.find_element_by_tag_name(pathValue)
        elif pathType.lower() == 'partial_link_text':
            return self.driver.find_element_by_partial_link_text(pathValue)

    def find_elements(self, name=None):
        pathType = self.elementRead.getPathType(name)
        pathValue = self.elementRead.getPathValue(name)
        if pathType == 'id':
            return self.driver.find_elements_by_id(pathValue)
        elif pathType == 'class_name':
            return self.driver.find_elements_by_class_name(pathValue)
        elif pathType == 'name':
            return self.driver.find_elements_by_name(pathValue)
        elif pathType == 'css_selector':
            return self.driver.find_elements_by_css_selector(pathValue)
        elif pathType == 'xpath':
            return self.driver.find_elements_by_xpath(pathValue)
        elif pathType == 'link_text':
            return self.driver.find_elements_by_link_text(pathValue)
        elif pathType == 'tag_name':
            return self.driver.find_elements_by_tag_name(pathValue)
        elif pathType == 'partial_link_text':
            return self.driver.find_elements_by_partial_link_text(pathValue)

    def element_is_exist(self, name):
        if len(self.find_elements(name)) == 0:
            return False
        return True

    def alter(self):
        return self.driver.switch_to.alert()

    def is_alter_present(self):
        try:
            self.driver.switch_to.alert()
            return True
        except Exception as e:
            print(e)
            return False


    # 鼠标右键
    def right_click(self, element_name=None):
        ac = ActionChains(self.driver)
        return ac.context_click(self.find_element(element_name)).perform()

    def forward(self):
        self.driver.forward()

    def back(self):
        self.driver.back()
if __name__ == '__main__':
    dr = Drive(1)
    dr.open_browser('http://www.multilotto.com/en')
    time.sleep(2)
    #dr.find_element("百度搜索输入框").send_keys("haha")
    print(dr.is_alter_present())
    dr.find_element("首页弹窗确认").click()
    time.sleep(10)
    print(dr.is_alter_present())
    dr.find_element("首页图标").click()
    #dr.close_brwser()