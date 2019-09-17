from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time 
# 发布帖子
driver = webdriver.Chrome()
driver.get('http://39.107.96.138:3000/signin')
driver.implicitly_wait(30)
driver.maximize_window()
# 进入发布话题页面
username = driver.find_element_by_id('name').send_keys('user1')
passwd = driver.find_element_by_id('pass').send_keys('123456')
loginbutton = driver.find_element_by_css_selector('input[type="submit"]').click()
topic = driver.find_element_by_css_selector('span[class="span-success"]').click()
selectblock = driver.find_element_by_css_selector('select[name="tab"]').click()
block = driver.find_element_by_css_selector('select[name="tab"]>option[value="share"]').click()
headline = driver.find_element_by_css_selector('textarea[class="span9"]').send_keys('test0917')
adit_area = driver.find_element_by_css_selector('div[class="CodeMirror-scroll"]')
adit_area.click()
# 操作快捷键
ActionChains(driver).move_to_element(adit_area).send_keys('abcd').perform()
ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).send_keys('b').key_up(Keys.CONTROL).perform()
# 对测试结果截图
driver.save_screenshot('./jietu/kuaijiejian.png')
# 提交话题
submit = driver.find_element_by_css_selector('input[type="submit"]')
submit.click()
# 对提交后的结果进行截图，判断是否发布成功
submit.save_screenshot('./jietu/topic.png')
time.sleep(3)
# 关闭窗口
driver.quit()