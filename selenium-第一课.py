from selenium import webdriver
for i in range(3):
    web=webdriver.Firefox()
    web.get("https:\\www.baidu.com")
    web.find_element_by_id("kw").send_keys("aaaa")
    web.find_element_by_id("su").click()
print(web.title)
