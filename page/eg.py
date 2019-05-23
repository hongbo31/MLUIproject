from common.basepage import BasePage
import time
from common.log import Log


class Example(BasePage):   # 页面的名称， 继承Basepage这个类

    def link_example_page(self):   #进入 这个页面的方法
        self.link_page("https://www.baidu.com")



if __name__ == '__main__':  # 这个是调试你这个类的方法
    duixiangming = Example()   # 实例化/创建这个类的对象，有对象了你才能调用这个类的方法，“对象名”就代表了方法里面的self
    duixiangming.link_example_page()