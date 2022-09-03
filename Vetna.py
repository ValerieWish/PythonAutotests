#авторизуюсь в тестовом аккаунте зоомагазина Ветна
import time
from selenium import webdriver

def test_setup():
    global driver
    driver = webdriver.Chrome()

def test_login():
    driver.get('https://vetna.info/')
    driver.maximize_window()
    driver.find_element("xpath", '//a[@title="Личный кабинет"]').click()
    driver.find_element("xpath", '//input[@id="login_auth_2020"]').send_keys('ТУТ ПОЧТА')
    driver.find_element("xpath", '//input[@id="parol_auth_2020"]').send_keys('ТУТ ПАРОЛЬ')
    driver.find_element("xpath", '//input[@value="Войти"]').click()

#проверка на наличие приветствия
def test_welcometext():
    content = driver.page_source
    result = content.find('Добро пожаловать, ТУТ ИМЯ!')
    print("Индекс найденного элемента:", result)

    if (result != -1):
        print("Найдено")
    else:
        print("Сломалось")
        print(content)

#добавляю новый основной адрес (любые данные)
def test_addaddress():
    driver.find_element("xpath", '//a[@href="/personal/adresa/"]').click()
    driver.find_element("xpath", '//button[@onclick="tema_adress();return false;"]').click()
    driver.find_element("xpath", '//input[@id="name_adress"]').send_keys('Домашний адрес')
    driver.find_element("xpath", '//input[@id="gorod_adress"]').send_keys('Москва')
    driver.find_element("xpath", '//input[@id="ulica_adress"]').send_keys('Морковно-ежевичная ул')
    driver.find_element("xpath", '//input[@id="dom_adress"]').send_keys('808')
    driver.find_element("xpath", '//input[@id="kv_adress"]').send_keys('1050')
    driver.find_element("xpath", '//span[@class="checkbox-custom-ld"]').click()
    driver.find_element("xpath", '//*[@id="popup_adress"]/div/div/div/div/div/button').click()
    time.sleep(2)

#проверка успешного добавления адреса
    content1 = driver.page_source
    result = content1.find('Ваш адрес добавлен!')
    print("Индекс найденного элемента:", result)

    if (result != -1):
        print("Найдено")
    else:
        print("Сломалось")
        print(content1)

#удаление ранее добавленного адреса
def test_deleteaddress():
    driver.find_element("xpath", '//*[@id="popup_adress"]/div/div/div/span').click()
    time.sleep(3)
    driver.find_element("xpath", '//div[@class="pinomci1-redakt pinomci1-udal"]').click()
    time.sleep(5)
    driver.quit()

test_setup()
test_login()
test_welcometext()
test_addaddress()
test_deleteaddress()