from dataclasses import dataclass


@dataclass
class LoanScenario:
    name: str
    loan_balance: str
    interest_rate: str
    compound_frequency: str   
    payback_frequency: str
    term_years: str = ""
    term_months: str = ""
    expected_monthly_payment: float = None   
    expected_tolerance: float = 0.05          


HAPPY_PATH_SCENARIOS = [
    LoanScenario(
        name="standard_5yr_loan",
        loan_balance="10000",
        interest_rate="6",
        compound_frequency="monthly",
        payback_frequency="month",
        term_years="5",
        term_months="0",
    ),
    LoanScenario(
        name="mortgage_style_30yr",
        loan_balance="300000",
        interest_rate="4.5",
        compound_frequency="monthly",
        payback_frequency="month",
        term_years="30",
        term_months="0",
    ),
    LoanScenario(
        name="auto_loan_3yr",
        loan_balance="25000",
        interest_rate="5.25",
        compound_frequency="monthly",
        payback_frequency="month",
        term_years="3",
        term_months="0",
    ),
]

EDGE_CASE_SCENARIOS = [
    LoanScenario(
        name="very_short_term_1_month",
        loan_balance="1000",
        interest_rate="5",
        compound_frequency="monthly",
        payback_frequency="month",
        term_years="0",
        term_months="1",
    ),
    LoanScenario(
        name="very_long_term_50yr",
        loan_balance="500000",
        interest_rate="3",
        compound_frequency="monthly",
        payback_frequency="month",
        term_years="50",
        term_months="0",
    ),
    LoanScenario(
        name="zero_interest_rate",
        loan_balance="5000",
        interest_rate="0",
        compound_frequency="monthly",
        payback_frequency="month",
        term_years="2",
        term_months="0",
    ),
    LoanScenario(
        name="very_high_interest_rate",
        loan_balance="5000",
        interest_rate="35",
        compound_frequency="monthly",
        payback_frequency="month",
        term_years="1",
        term_months="0",
    ),
    LoanScenario(
        name="very_small_loan_balance",
        loan_balance="10",
        interest_rate="5",
        compound_frequency="monthly",
        payback_frequency="month",
        term_years="1",
        term_months="0",
    ),
    LoanScenario(
        name="large_loan_balance",
        loan_balance="10000000",
        interest_rate="4",
        compound_frequency="monthly",
        payback_frequency="month",
        term_years="30",
        term_months="0",
    ),
    LoanScenario(
        name="fractional_interest_rate",
        loan_balance="15000",
        interest_rate="4.375",
        compound_frequency="monthly",
        payback_frequency="month",
        term_years="4",
        term_months="0",
    ),
    LoanScenario(
        name="years_and_months_combined",
        loan_balance="20000",
        interest_rate="6.5",
        compound_frequency="monthly",
        payback_frequency="month",
        term_years="2",
        term_months="6",
    ),
]