
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains  # 破解滑动验证码的时候用的 可以拖动图片
from selenium.webdriver.support.ui import WebDriverWait  # 引用设定显示等待时间
import random
from selenium.webdriver.chrome.options import Options  # selenium启动浏览器时常用的属性
import os
chrome_options = Options()
chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
# 禁用 WebGL，在不显示窗口的模式下，也不显示错误消息。
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-software-rasterizer')
chrome_options.add_argument(
    '-enable-webgl --no-sandbox --disable-dev-shm-usage')

# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# time.sleep(2)
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
# time.sleep(1)

# driver.quit()

# ————————————百度云大类————————————————


class baiduSEM(object):

    def __init__(self, name, list, cat, cat_lists, num, path):
        # self.driver = webdriver.Chrome()  # 实例化浏览器对象，并命名为 browser
        self.driver = webdriver.Chrome(options=chrome_options)
        self.name = name
        self.list = list
        self.cat = cat
        self.cat_lists = cat_lists
        self.num = num
        self.path = path
        self.wait = WebDriverWait(self.driver, 10)  # 设定浏览器最大等待时间为5秒钟，超过就报错

        for i in range(self.num):
            self.get_catlists()
            print("执行一次")
            time.sleep(1)
        # 关闭浏览器
        self.driver.quit()


# ————————————获取一个的url————————————


    def get_url(self):
        self.driver.get('https://www.baidu.com/')
        time.sleep(2)
        self.driver.find_element_by_id("kw").send_keys(self.name)
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
        self.get_file()
        time.sleep(1)
        self.driver.quit()

# ————————————获取多个的页面————————————
    def get_list(self):
        self.driver.get('https://www.baidu.com/')
        time.sleep(2)
        for i in self.list:
            self.driver.find_element_by_id("kw").clear()
            self.driver.find_element_by_id("kw").send_keys(i)
            time.sleep(1)
            self.driver.find_element_by_id("su").click()
            time.sleep(3)
            # 判断加载是否完成   文档协作_百度搜索
            title = self.driver.title
            if title != (str(i)+'_百度搜索'):
                self.driver.refresh()
                time.sleep(8)
            source = self.driver.page_source
            f = open('E:/py/baiduSEM/file'+str(i) +
                     '.html', mode="w", encoding="utf-8")
            f.write(source)
            f.close()
            time.sleep(1)
        self.driver.quit()

# ————————————获取有分类页面————————————
    def get_catlists(self):
        self.driver.get('https://www.baidu.com/')
        time.sleep(2)
        path_op = self.path
        num = 0
        num1 = 1
        for line in cat_lists:
            print(cat[num])
            for i in line:
                self.driver.find_element_by_id("kw").clear()
                self.driver.find_element_by_id("kw").send_keys(i)
                time.sleep(1)
                self.driver.find_element_by_id("su").click()
                time.sleep(1)
                # 判断加载是否完成   文档协作_百度搜索
                title = self.driver.title
                if title != (str(i)+'_百度搜索'):
                    self.driver.refresh()
                    time.sleep(3)
                title = self.driver.title
                if title != (str(i)+'_百度搜索'):
                    self.driver.refresh()
                    time.sleep(8)
                title = self.driver.title
                if title != (str(i)+'_百度搜索'):
                    self.driver.refresh()
                    time.sleep(3)
                title = self.driver.title
                if title != (str(i)+'_百度搜索'):
                    self.driver.refresh()
                    time.sleep(8)
                title = self.driver.title
                if title != (str(i)+'_百度搜索'):
                    self.driver.refresh()
                    time.sleep(3)
                title = self.driver.title
                if title != (str(i)+'_百度搜索'):
                    self.driver.refresh()
                    time.sleep(3)
                title = self.driver.title
                if title != (str(i)+'_百度搜索'):
                    self.driver.refresh()
                    time.sleep(3)
                title = self.driver.title
                if title != (str(i)+'_百度搜索'):
                    self.driver.refresh()
                    time.sleep(3)

                source = self.driver.page_source
                # 储存的格式为 分类名称_分类子项
                # f = open('E:/py/baiduSEM/'+str(self.cat[num])+'_'+str(i) +
                #          '.html', mode="w", encoding="utf-8")
                # 储存的变成数字
                # f = open('E:/py/baiduSEM/'+str(num1) +
                #          '.html', mode="w", encoding="utf-8")

                path = str(path_op)+str(self.cat[num])+"/"+str(i)+"/"
                if not os.path.exists(path):
                    os.makedirs(path)
                # 储存的格式为 分类名称_分类子项
                # time.sleep(1)

                now = int(round(time.time()*1000))
                now02 = time.strftime(
                    '%Y-%m-%d-%H-%M-%S', time.localtime(now/1000))
                f = open(str(path_op)+str(self.cat[num])+"/"+str(i) + "/"+now02 +
                         '.html', mode="w", encoding="utf-8")
                f.write(source)
                f.close()

                num1 += 1
                time.sleep(1)
            num += 1


# ————————————获取当前文件保存————————————


    def get_file(self):
        source = self.driver.page_source
        f = open('E:/py/baiduSEM/'+str(self.name) +
                 '.html', mode="w", encoding="utf-8")
        f.write(source)
        f.close()


# ———————————主体参数———————————————————————
if __name__ == '__main__':
    name = "天地"
    list = ['用户标签系统', 'ETL工具']
    # 循环次数
    num = 1
    path = "D:/py/selenium/baiduSEM3/"  # 这个是要存储的路径
    # cat = ['数据集成', 'BI', '营销自动化', '在线客服']
    # cat_数据集成 = ['数据集成', '数据融合', '多源异构数据集成', '数据集成工具', 'ETL', 'ETL工具']
    # cat_BI = ['BI工具', 'BI商业智能', '商业智能软件', 'BI工具有哪些', 'BI系统']
    # cat_营销自动化 = ['营销自动化', '营销自动化工具', '自动化营销系统', '用户标签系统', '用户画像系统']
    # cat_在线客服 = ['在线客服系统', '在线客服', '在线客服软件', '客服软件', '在线客服工具']
    # cat_lists = [cat_数据集成, cat_BI, cat_营销自动化, cat_在线客服]

    # 分类列表 cat 分类的关键词数据
    cat = []
    cat_lists = []
    with open("D:\py\selenium\sem.txt", "r", encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip('\n')
            line_str = line.split('：', 1)  # 去掉列表中每一个元素的换行符
            # print(line_str[0])
            cat.append(line_str[0])
            line_str[0] = []
            for li in line_str[1].split('，'):
                # print(li)
                (line_str[0]).append(li)
            cat_lists.append(line_str[0])
    print(cat)
    print(cat_lists)
    # 循环

    window = baiduSEM(name, list, cat, cat_lists, num, path)
