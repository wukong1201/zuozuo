import os,sys

import allure
import pytest

from page.setting_page import SettingPage

sys.path.append(os.getcwd())
from base.init_driver import get_driver
from base.read_yaml import read_yaml_data
import page

#读取sms_send.yaml的数据
def get_data():
    data =  read_yaml_data("setting_send.yaml")
    return  data.get("send_data")

class TestSms:

    def setup_class(self):
        #1.初始化driver
        self.driver = get_driver()
        #2.初始化smspage类
        self.settingpage = SettingPage(self.driver)
    def teardown_class(self):
        # 1 退出driver
        self.driver.quit()
        #点击搜索圈

    @allure.step(title='测试设置搜索')
    @allure.attach("搜索，增加")
    def test_click_search_btn(self):
        # 1.点击新增按钮
        self.settingpage.click_search_btn()
    @pytest.mark.parametrize("content",get_data())
            #向搜索框内输入1/2/3
    def test_input_number_search(self,content):
        self.settingpage.input_number_search(content)
        #按返回键
    def test_click_back_butn(self):
        self.settingpage.click_back_butn()





