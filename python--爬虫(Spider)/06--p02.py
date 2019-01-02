from selenium import webdriver
import time

# 通过Keys模拟键盘
from selenium.webdriver.common.keys import Keys

# 可能需要手动添加路径
driver = webdriver.Chrome()
url = "http://www.baidu.com"
driver.get(url)

# .text-->显示文字(自己查阅一下)
text = driver.find_element_by_id("wrapper").text
print(text)

print(driver.title)
# 得到页面的快照
driver.save_screenshot("index.png")

# 在百度的搜索框(id="kw")内输入"大熊猫"
driver.find_element_by_id("kw").send_keys(u"大熊猫")
# 模拟点击搜索按钮(id="su")
driver.find_element_by_id("su").click()

time.sleep(5)
# 截屏
driver.save_screenshot("大熊猫.png")

# 获得当前页面的cookie
print(driver.get_cookies())

# 模拟输入ctrl+a: 全选
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "a")
# 模拟输入ctrl+x: 剪切
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "x")

driver.find_element_by_id("kw").send_keys(u"航空母舰")
driver.save_screenshot("航空母舰1.png")
driver.find_element_by_id("su").send_keys(Keys.RETURN)

time.sleep(5)
driver.save_screenshot("航空母舰2.png")

# 清空搜索框,退出浏览器
driver.find_element_by_id("kw").clear()
driver.save_screenshot("清空浏览器.png")
driver.quit()