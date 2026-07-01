from playwright.sync_api import Page, expect

def test_price_low_to_high_sorts_correctly(page: Page):
    # 1. standart_user log in
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    # 2. Price (low to high)
    page.locator("[data-test=\"product-sort-container\"]").select_option("lohi")

    # 3. READ PRICES
    price_texts = page.locator("[data-test=\"inventory-item-price\"]").all_inner_texts()

    prices = [float(p.replace("$", "")) for p in price_texts]

    # 4. VERIFY
    assert prices == sorted(prices)