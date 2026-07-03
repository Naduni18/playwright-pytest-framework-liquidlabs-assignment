def calculate_monthly_payment(principal: float, annual_rate_pct: float,
                               total_months: int) -> float:
    
    if total_months <= 0:
        raise ValueError("total_months must be > 0")

    if annual_rate_pct == 0:
        return round(principal / total_months, 2)

    r = (annual_rate_pct / 100) / 12
    factor = (1 + r) ** total_months
    payment = principal * r * factor / (factor - 1)
    return round(payment, 2)


def calculate_total_payment(monthly_payment: float, total_months: int) -> float:
    return round(monthly_payment * total_months, 2)


def calculate_total_interest(total_payment: float, principal: float) -> float:
    return round(total_payment - principal, 2)


def parse_currency(value: str) -> float:
    cleaned = value.replace("$", "").replace(",", "").strip()
    return float(cleaned)