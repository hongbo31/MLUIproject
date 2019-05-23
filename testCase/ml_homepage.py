import unittest
from common.drive import Drive
from common.log import Log
from common.elementRead import ElementsRead
from common.screen import Screen
import time

class Test_Homepage(unittest.TestCase):

    def setUp(self):
        self.drive = Drive(1)
        self.log = Log()
        self.url = "http://www.multilotto.com/en"
        self.readconfig = ElementsRead()

    def test_go_to_homepage(self):
        self.log.info("开始测试，进入首页")
        self.drive.open_browser(self.url)
        time.sleep(3)

        self.log.info("点击左上角图标，刷新首页")
        self.drive.find_element("首页图标").click()

    def tearDown(self):
        self.log.info("测试结束")
        time.sleep(10)
        self.drive.close_brwser()


if __name__ == '__main__':
    unittest.main()