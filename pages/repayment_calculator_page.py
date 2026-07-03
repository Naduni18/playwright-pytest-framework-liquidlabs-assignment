from playwright.sync_api import Page
from pages.base_page import BasePage


class RepaymentCalculatorPage(BasePage):

    URL = "https://www.calculator.net/repayment-calculator.html"


    LOAN_BALANCE_INPUT = "#cloanamount"
    INTEREST_RATE_INPUT = "#cinterestrate"
    COMPOUND_SELECT = "#ccompound"
    PAYBACK_SELECT = "#cpayback"
    FIXED_TERM_RADIO = "#cpaybackway1"          
    FIXED_INSTALLMENT_RADIO = "#cpaybackway2"   
    FIXED_TERM_YEARS_INPUT = "#cyears"
    FIXED_TERM_MONTHS_INPUT = "#cmonths"
    FIXED_INSTALLMENT_INPUT = "#cpaybackwayamt"
    CALCULATE_BUTTON = "input[value='Calculate']"
    RESULT_MONTHLY_PAYMENT = "div.rightresult table tbody tr:nth-child(1) td:nth-child(2)"
    RESULT_TOTAL_PAYMENTS = "div.rightresult table tbody tr:nth-child(2) td:nth-child(2)"
    RESULT_TOTAL_INTEREST = "div.rightresult table tbody tr:nth-child(3) td:nth-child(2)"
    RESULT_ERROR_MESSAGE = "div.rightresult div div font"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        self.goto(self.URL)
        return self

    def set_loan_balance(self, amount: str):
        self.clear_and_fill(self.LOAN_BALANCE_INPUT, amount)
        return self

    def set_interest_rate(self, rate: str):
        self.clear_and_fill(self.INTEREST_RATE_INPUT, rate)
        return self

    def set_compound_frequency(self, label_text: str):
        self.page.locator(self.COMPOUND_SELECT).select_option(value=label_text)
        return self

    def set_payback_frequency(self, label_text: str):
        self.page.locator(self.PAYBACK_SELECT).select_option(value=label_text)
        return self

    def choose_fixed_term_mode(self):
        self.page.locator(self.FIXED_TERM_RADIO).check()
        return self

    def choose_fixed_installment_mode(self):
        self.page.locator(self.FIXED_INSTALLMENT_RADIO).check()
        return self

    def set_fixed_term(self, years: str = "", months: str = ""):
        self.choose_fixed_term_mode()
        if years:
            self.clear_and_fill(self.FIXED_TERM_YEARS_INPUT, years)
        if months:
            self.clear_and_fill(self.FIXED_TERM_MONTHS_INPUT, months)
        return self

    def click_calculate(self):
        self.page.locator(self.CALCULATE_BUTTON).click()
        self.page.wait_for_load_state("domcontentloaded")
        return self

    # --- Results --------------------------------------------------
    def get_monthly_payment(self) -> str:
        return self.get_text(self.RESULT_MONTHLY_PAYMENT)

    def get_total_payments(self) -> str:
        return self.get_text(self.RESULT_TOTAL_PAYMENTS)

    def get_total_interest(self) -> str:
        return self.get_text(self.RESULT_TOTAL_INTEREST)

    def get_all_results(self) -> dict:
        return {
            "monthly_payment": self.get_monthly_payment(),
            "total_payments": self.get_total_payments(),
            "total_interest": self.get_total_interest(),
        }
        
    def get_error_message(self) -> str:
        return self.get_text(self.RESULT_ERROR_MESSAGE)