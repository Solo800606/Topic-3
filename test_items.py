# Запуск pytest --language=es test_items.py
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_presence_of_the_Add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    browser.find_elements_by_css_selector("language.form-control")
    
    text_elt = browser.find_element_by_css_selector(".btn-add-to-basket")
    text_basket = text_elt.text
    assert "Añadir al carrito" == text_basket

