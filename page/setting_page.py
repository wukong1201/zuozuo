from base.base_action import BaseAction
import page
class SettingPage(BaseAction):
    #初始化方法
    def __init__(self,driver):
        BaseAction.__init__(self,driver)
    #把要测试的整个业务分为多个函数实现
    #1点击搜索圈
    def click_search_btn(self):
        self.click_element(page.set_search)

    #2向接收着输入框里面输入内容
    def input_number_search(self,number):
        self.input_num_content(page.set_text_input,number)

    #3 返回
    def click_back_butn(self):
        #3.1 动态向发送框 输入了一个内容
        self.click_element(page.set_click_back)



