'''
1. Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
2. Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя. Браузер должен объявляться
в фикстуре browser и передаваться в тест как параметр.
3. В файл test_main_page.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину
Например, можно проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
4. Тест должен запускаться с параметром language следующей командой:
pytest --language=es test_main_page.py
'''
from selenium.webdriver.common.by import By
from time import sleep


def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()


def test_add_button_should_be_displayed(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    go_to_login_page(browser)
