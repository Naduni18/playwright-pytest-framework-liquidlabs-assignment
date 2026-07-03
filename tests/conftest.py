import pytest
from pages.repayment_calculator_page import RepaymentCalculatorPage


@pytest.fixture
def calculator_page(page):
    calc_page = RepaymentCalculatorPage(page)
    calc_page.open()
    return calc_page


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1366, "height": 900},
    }