import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_presence_of_the_Add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    button = None
    try:
        button = browser.find_element_by_class_name('btn-add-to-basket')
    except NoSuchElementException:
        pass
    assert button!=None, 'Should be button add to basket'
    
