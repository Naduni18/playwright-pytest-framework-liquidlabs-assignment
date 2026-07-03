# Repayment Calculator Test Suite - Playwright pytest Framework

Automated tests for https://www.calculator.net/repayment-calculator.html
using Python, Pytest, and Playwright.

## Architecture
1. `pages/`   : Page Object Model (all locators & UI actions live here)
2. `data/`    : Test data as dataclasses, decoupled from test logic
3. `tests/`   : Test cases (assertions only, no locators)
4. `utils/`   : Independent amortization-math helper used to verify the
               site's output against an standard formula

## Setup
1. Python 3.9+
2. `python -m venv venv && source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `playwright install`

## Running tests
1. All tests: `pytest`
2. Smoke only: `pytest -m smoke`
3. Edge cases only: `pytest -m edge`
4. Headed mode: `pytest --headed`

## HTML report: 
  generated automatically at `report.html`

## Notes:
  Assertions use `pytest.approx` with tolerance because calculator.net rounds displayed values, so exact float equality isn't reliable.

## Math formulas used

### The core formula: Monthly Payment (Amortization Formula)

This is the formula used in `calculate_monthly_payment()` in `utils/financial_helper.py`. It's the standard formula for a fixed-rate, fully amortizing loan (this is the same formula banks use for mortgages, auto loans, personal loans, etc.).

$$
M = P \times \frac{r(1+r)^n}{(1+r)^n - 1}
$$

#### Why the rate gets divided down:
The interest rate on a loan is always quoted annually (e.g., "6% APR"), but payments happen monthly. So before using it in the formula, you convert:

$$
r = \frac{\text{annual rate}/100}{12}
$$

### Special case: 0% Interest Rate
If r = 0, the formula above breaks — you'd be dividing by (factor - 1), which becomes (1 - 1) = 0, causing a divide-by-zero crash.
But mathematically, at 0% interest, there's no compounding at all — you're just splitting the debt evenly:

$$
M = \frac{P}{n}
$$

### Total Amount Paid
Once you know the monthly payment, the total paid over the life of the loan is simply:

$$
\text{Total Paid} = M \times n
$$

You're paying the same amount M, every month, for n months.

### Total Interest Paid
Whatever you paid beyond the original loan amount is the interest:

$$
\text{Total Interest}=\text{Total Paid}−P
$$

#### Variables:

M = monthly payment (what you're solving for)

P = principal (the loan balance — how much was borrowed)

r = monthly interest rate, as a decimal (not the annual rate!)

n = total number of monthly payments (loan term in months)