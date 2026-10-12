# Both functions: O(1) time/space for fixed-size numeric inputs.

MINIMUM_CREDITS = 120
MINIMUM_GPA = 2.0


def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= MINIMUM_CREDITS and gpa >= MINIMUM_GPA


def missing(credits: int, gpa: float) -> list[str]:
    reasons: list[str] = []
    if credits < MINIMUM_CREDITS:
        missing_credits = MINIMUM_CREDITS - credits
        credit_label = "credit" if missing_credits == 1 else "credits"
        reasons.append(f"need {missing_credits} more {credit_label}")
    if gpa < MINIMUM_GPA:
        reasons.append(f"need GPA of at least {MINIMUM_GPA}")
    return reasons
