#Пайтест на авторизацию в онлайн-магазине, поиск по сайту и добавление в корзину + аллюр с декораторами для отчета

import allure
from selenium import webdriver
from selenium.webdriver import Keys
import time

@allure.title("Подготовка вебдрайвера")
def test_setup():
    global driver
    driver = webdriver.Chrome("C:\\Users\\USER\\PycharmProjects\\AUTOTEST\\NewTests\\chromedriver.exe")

@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Тест авторизации")
@allure.description("Проверка возможности авторизации на сайте")
def test_login():
    driver.get('http://sandbox.synctoskill.com/')
    driver.maximize_window()
    driver.find_element("xpath", '//*[@href="/Account/Login?returnUrl=%2F"]').click()
    driver.find_element("xpath", '//input[@name="Email"]').send_keys('ТУТ ПОЧТА')
    driver.find_element("xpath", '//input[@name="Password"]').send_keys('ТУТ ПАРОЛЬ')
    driver.find_element("xpath", '//input[@value="Sign In"]').click()
    time.sleep(2)
    driver.find_element("xpath", '//a[@href="/Account/Profile" and contains (@style, "padding:0")]').get_attribute('text').find('ТУТ ИМЯ ЮЗЕРА')

@allure.severity(allure.severity_level.NORMAL)
@allure.title("Тест поиска")
@allure.description("Проверка возможности нахождения товара через строку поиска")
def test_search():
    driver.find_element("xpath", '//input[@placeholder="Search..."]').send_keys('Broccoli')
    driver.find_element("xpath", '//input[@placeholder="Search..."]').send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element("xpath", '//a[@href="/Product/Index/3"]').get_attribute('text').find('Broccoli')

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест корзины")
@allure.description("Проверка возможности добавления товара в корзину")
def test_addtocart():
    driver.find_element("xpath", '//input[@value="Add to cart"]').click()
    driver.find_element("xpath", '//i[@class="fa fa-shopping-cart"]').click()
    time.sleep(2)
    driver.find_element("xpath", '//a[@href="/Product/Index/3"]').get_attribute('text').find('Broccoli')
    driver.quit()

