import pytest
from data.test_data import EDGE_CASE_SCENARIOS
from utils.financial_helper import calculate_monthly_payment, parse_currency


@pytest.mark.edge
@pytest.mark.parametrize("scenario", EDGE_CASE_SCENARIOS, ids=lambda s: s.name)
def test_edge_case_scenarios(calculator_page, scenario):
    calculator_page.set_loan_balance(scenario.loan_balance)
    calculator_page.set_interest_rate(scenario.interest_rate)
    calculator_page.set_compound_frequency(scenario.compound_frequency)
    calculator_page.set_payback_frequency(scenario.payback_frequency)
    calculator_page.set_fixed_term(scenario.term_years, scenario.term_months)
    calculator_page.click_calculate()

    results = calculator_page.get_all_results()
    actual_monthly = parse_currency(results["monthly_payment"])

    total_months = int(scenario.term_years) * 12 + int(scenario.term_months or 0)
    expected_monthly = calculate_monthly_payment(
        float(scenario.loan_balance), float(scenario.interest_rate), total_months
    )

    assert actual_monthly == pytest.approx(expected_monthly, rel=0.03), (
        f"[{scenario.name}] Expected ~{expected_monthly}, got {actual_monthly}"
    )
    assert actual_monthly > 0, f"[{scenario.name}] Monthly payment should be > 0"


@pytest.mark.edge
def test_zero_loan_balance_shows_validation_or_zero(calculator_page):
    calculator_page.set_loan_balance("0")
    calculator_page.set_interest_rate("5")
    calculator_page.set_compound_frequency("monthly")
    calculator_page.set_payback_frequency("month")
    calculator_page.set_fixed_term(years="5")
    calculator_page.click_calculate()

    results = calculator_page.get_error_message()
    assert results, "Please provide a positive loan balance amount."


@pytest.mark.edge
def test_negative_interest_rate_is_rejected_or_handled(calculator_page):
    calculator_page.set_loan_balance("10000")
    calculator_page.set_interest_rate("-5")
    calculator_page.set_compound_frequency("monthly")
    calculator_page.set_payback_frequency("month")
    calculator_page.set_fixed_term(years="5")
    calculator_page.click_calculate()

    
    results = calculator_page.get_error_message()
    assert results, "Please provide a positive interest rate value."