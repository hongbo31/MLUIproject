import xml.etree.cElementTree as ET
from common.getfilepath import get_path
import os


class ElementsRead:

    def __init__(self):
        xml_file_path = os.path.join(get_path(), '../testFile/config.xml')  # 文件路径, 在当前目录下的上一层路径的/testFile文件下面
        self.tree = ET.parse(xml_file_path)
        self.root = self.tree.getroot()

    # 获取所有元素name，type，value，返回一个二维列表
    def get_all_elements(self):
        elements = []
        for children in self.root.findall('element'):
            name = children.find('name').text
            path_type = children.find('pathType').text
            path_value = children.find('pathValue').text
            t = [name, path_type, path_value]
            elements.append(t)
        return elements

        # 获取所有元素的name， 返回一个list
    def get_all_elements_name(self):
        temp_list = ElementsRead().get_all_elements()
        name_list = []
        for i in temp_list:
            name = i[0]
            name_list.append(name)
        return name_list

        # 根据元素的name，返回元素的定位方式path，如果元素不存在则返回none
    def getPathType(self, name):
        path_type_list = ElementsRead().get_all_elements()
        for i in path_type_list:
            if i[0] == name:
                return i[1]

        # 根据xml文件的name， 返回元素定位的value，如果元素不存在则返回none
    def getPathValue(self, name):
        path_value_list = ElementsRead().get_all_elements()
        for i in path_value_list:
            if i[0] == name:
                return i[2]


if __name__ == '__main__':
    r1 = ElementsRead()
    print(r1.get_all_elements())
    print(r1.get_all_elements_name())
