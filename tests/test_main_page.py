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
from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

