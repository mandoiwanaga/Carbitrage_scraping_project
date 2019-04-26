


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
    
    
def get_css_title(browser):
    """Return car title"""
    css_title = 'div.page h2.listing-row__title'
    titles = browser.find_elements_by_css_selector(css_title)
    list_titles = [title.text for title in titles]
    return list_titles
    
    
def get_next_page(browser):
    """Go to next page"""
    css_next_page = 'Next'
    next_page = browser.find_element_by_link_text(css_next_page)
    next_page.click()