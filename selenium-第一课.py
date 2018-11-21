from selenium import webdriver
for i in range(1):
    web=webdriver.Firefox()
    web.get("https:\\www.baidu.com")
    web.find_element_by_id("kw").send_keys("aaaa")
    web.find_element_by_id("su").click()
    web.quit()
print(web.title)
