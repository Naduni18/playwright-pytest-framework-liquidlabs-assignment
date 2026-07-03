from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")

    def clear_and_fill(self, selector: str, value: str):
        locator = self.page.locator(selector)
        locator.click()
        locator.clear()
        locator.fill(value)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text().strip()