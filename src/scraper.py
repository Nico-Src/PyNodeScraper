from playwright.sync_api import sync_playwright

class Scraper():
    def __init__(self): pass

    # scrape url
    def scrape_url(self, url, callback):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            # take screenshot and save it to disk
            screen = page.screenshot(path=f'img/screen.jpg');
            browser.close();
            # call callback if there is one
            if callback is not None: callback(screen);
