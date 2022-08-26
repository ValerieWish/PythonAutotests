#Здесь добываю список новостей с главной страницы Яндекса и отражаю их в терминале

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://yandex.ru/')
newsHeaders = driver.find_elements("xpath", '//span[@class = "news__item-content"]')
for i in newsHeaders:
    print(i.text)
driver.close()

