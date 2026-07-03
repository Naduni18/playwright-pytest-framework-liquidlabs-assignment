import pytest
from data.test_data import HAPPY_PATH_SCENARIOS
from utils.financial_helper import (
    calculate_monthly_payment,
    calculate_total_payment,
    calculate_total_interest,
    parse_currency,
)


@pytest.mark.smoke
@pytest.mark.parametrize("scenario", HAPPY_PATH_SCENARIOS, ids=lambda s: s.name)
def test_monthly_payment_fixed_term(calculator_page, scenario):
    calculator_page.set_loan_balance(scenario.loan_balance)
    calculator_page.set_interest_rate(scenario.interest_rate)
    calculator_page.set_compound_frequency(scenario.compound_frequency)
    calculator_page.set_payback_frequency(scenario.payback_frequency)
    calculator_page.set_fixed_term(scenario.term_years, scenario.term_months)
    calculator_page.click_calculate()

    results = calculator_page.get_all_results()
    actual_monthly = parse_currency(results["monthly_payment"])
    actual_total = parse_currency(results["total_payments"])
    actual_interest = parse_currency(results["total_interest"])

    total_months = int(scenario.term_years) * 12 + int(scenario.term_months or 0)
    expected_monthly = calculate_monthly_payment(
        float(scenario.loan_balance), float(scenario.interest_rate), total_months
    )
    expected_total = calculate_total_payment(expected_monthly, total_months)
    expected_interest = calculate_total_interest(expected_total, float(scenario.loan_balance))

    assert actual_monthly == pytest.approx(expected_monthly, rel=0.02), (
        f"[{scenario.name}] Monthly payment mismatch: "
        f"site={actual_monthly}, expected~={expected_monthly}"
    )
    assert actual_total == pytest.approx(expected_total, rel=0.02), (
        f"[{scenario.name}] Total payment mismatch: "
        f"site={actual_total}, expected~={expected_total}"
    )
    assert actual_interest == pytest.approx(expected_interest, rel=0.05), (
        f"[{scenario.name}] Interest mismatch: "
        f"site={actual_interest}, expected~={expected_interest}"
    )
    assert actual_total == pytest.approx(
        actual_monthly * total_months, rel=0.01
    ), f"[{scenario.name}] Internal consistency failed: monthly*n != total"


@pytest.mark.smoke
def test_results_are_populated_and_positive(calculator_page):
    calculator_page.set_loan_balance("10000")
    calculator_page.set_interest_rate("6")
    calculator_page.set_compound_frequency("monthly")
    calculator_page.set_payback_frequency("month")
    calculator_page.set_fixed_term(years="5")
    calculator_page.click_calculate()

    results = calculator_page.get_all_results()
    for key, val in results.items():
        assert val, f"{key} was empty"
        assert parse_currency(val) > 0, f"{key} was not positive: {val}"