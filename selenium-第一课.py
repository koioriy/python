from selenium import webdriver
for i in range(3):
    web=webdriver.Firefox()
    web.get("https:\\www.baidu.com")
print(web.title)