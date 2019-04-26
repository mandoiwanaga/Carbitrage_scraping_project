


def get_css_price(browser):
    """Return the price"""
    css_price = 'div.page span.listing-row__price'
    prices = browser.find_elements_by_css_selector(css_price)
    list_prices = [price.text for price in prices]
    return list_prices
    
    
def get_css_mileage(browser):
    """Return mileage"""
    css_mileage = 'div.page span.listing-row__mileage'
    mileages = browser.find_elements_by_css_selector(css_mileage)
    list_mileages = [mileage.text for mileage in mileages]
    return list_mileages
    
    
def get_css_title_and_year(browser):
    """Return car title"""
    css_title = 'div.page h2.listing-row__title'
    titles = browser.find_elements_by_css_selector(css_title)
    list_years = [str(year.text)[:4] for year in titles]
    list_titles = [title.text for title in titles]
    return list_titles, list_years
    
def get_next_page(browser):
    """Go to next page"""
    from selenium.webdriver.common.keys import Keys
    css_next_page = 'div.page a.button.next-page'
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    next_page = browser.find_element_by_css_selector(css_next_page)
    next_page.click()